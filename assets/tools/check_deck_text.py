"""C4 檢查：deck.html 上看得到的每一段文字，都必須出現在 03-content.md。
用法：python assets/tools/check_deck_text.py slides/<deck資料夾>
裝飾用的元素（.hanko 印章字、只有符號的節點）不檢查。"""
import re, sys, html
from html.parser import HTMLParser

folder = sys.argv[1].rstrip('/').rstrip(chr(92))
content = open(f'{folder}/03-content.md', encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', '', html.unescape(s))
C = norm(content)

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.inbody=False; s.skip=0; s.nodes=[]; s.slide=0
    def handle_starttag(s, t, a):
        a=dict(a)
        if t=='body': s.inbody=True
        if t=='section': s.slide+=1
        if t in('script','style') or 'hanko' in (a.get('class') or ''): s.skip+=1; s.stack.append((t,True))
        elif t not in('br','img','meta','link'): s.stack.append((t,False))
    def handle_endtag(s, t):
        while s.stack:
            tag,sk=s.stack.pop()
            if sk: s.skip-=1
            if tag==t: break
    def handle_data(s, d):
        if s.inbody and not s.skip:
            t=d.strip()
            if t and re.search(r'[\w一-鿿]', t): s.nodes.append((s.slide,t))

p=P(); p.feed(open(f'{folder}/deck.html', encoding='utf-8').read())
bad=[(n,t) for n,t in p.nodes if norm(t) not in C]
print(f'文字節點 {len(p.nodes)} 個，投影片 {p.slide} 頁')
if bad:
    print(f'不在 03-content.md 裡的文字：{len(bad)} 個')
    for n,t in bad: print(f'  第 {n} 頁：{t}')
else:
    print('全部都在 03-content.md 裡 ✅')
