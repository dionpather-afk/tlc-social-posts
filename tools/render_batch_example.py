import sys,re,json,asyncio
sys.path.insert(0,'/home/claude/gen')
import importlib.util
spec=importlib.util.spec_from_file_location('m','/home/claude/gen/make.py')
src=open('/home/claude/gen/make.py').read().split("import os\nos.chdir")[0]
ns={}; exec(src,ns)
poster,days=ns['poster'],ns['days']
day1=dict(file='Day1-Found.dc.html',title='Day 1',eyebrow='When customers search for you',h1a='Do they find you,',h1b='or your competitor?',body='One team for your whole online presence, on Google and in AI search. You run your business. We handle the rest.',items=['Website design and build','Domain registration','Hosting','Business email addresses','SEO: found on Google','AEO: found in AI answers','Analytics','Website health checks','Maintenance and updates','WhatsApp chat built in'],chipSize=24,h1Size=68)
NEW=[
dict(lead='green',file='x',title='Fri 06:00',eyebrow='Open 24/7',h1a='Your website works',h1b='while you sleep.',body='Customers search at night, on weekends and on public holidays. Your website answers them, takes their enquiry and sends them to your WhatsApp.',items=['Enquiry forms','WhatsApp chat built in','Works on every phone','Found on Google'],cta='Get yours started'),
dict(lead='yellow',file='x',title='Fri 12:00',eyebrow='Thinking about a website?',h1a='Tell us what you need.',h1b="We'll handle the rest.",body='Fill in a short form in your own words. No tech knowledge needed. We come back to you with a plan and a quote.',items=['A short, simple form','Plain-English advice','Design, build and hosting','Ongoing care and support'],cols=1,cta='Fill in the form'),
]
alld=NEW
FONTS='''@font-face{font-family:Syne;font-weight:700;src:url(node_modules/@fontsource/syne/files/syne-latin-700-normal.woff2)}
@font-face{font-family:Syne;font-weight:800;src:url(node_modules/@fontsource/syne/files/syne-latin-800-normal.woff2)}
@font-face{font-family:Inter;font-weight:400;src:url(node_modules/@fontsource/inter/files/inter-latin-400-normal.woff2)}
@font-face{font-family:Inter;font-weight:600;src:url(node_modules/@fontsource/inter/files/inter-latin-600-normal.woff2)}
@font-face{font-family:Inter;font-weight:700;src:url(node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2)}'''
def static(h, vertical):
    h=h.replace('<script src="./support.js"></script>','')
    h=re.sub(r'<link[^>]*fonts\.g[^>]*>','',h)
    h=h.replace('<x-dc>','').replace('</x-dc>','').replace('<helmet>','').replace('</helmet>','')
    h=re.sub(r'<script type="text/x-dc".*?</script>','',h,flags=re.S)
    h=h.replace('{{ footerLeft }}','Link in bio').replace('/_blob/1195e0fa49338d91f8364d3ed921bb53','tlc-logo.png')
    h=h.replace('<style>','<style>'+FONTS)
    if vertical:
        h=h.replace('width: 1080px; height: 1350px','width: 1018px; height: 1811px; zoom: 1.06').replace('padding: 64px 72px','padding: 160px 66px 300px 66px').replace('gap: 34px','gap: 44px').replace('width: 1080px; height: 16px','width: 1018px; height: 16px').replace('height: 1350px; background','height: 1811px; background')
    return h
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        out=[]
        for i,d in enumerate(alld,1):
            for v in (False,True):
                html=static(poster(d),v)
                fn=f'new{i}-{"vertical" if v else "feed"}'
                open(fn+'.html','w').write(html)
                await pg.set_viewport_size({'width':1080,'height':1920 if v else 1350})
                await pg.goto('file:///home/claude/render/'+fn+'.html'); await pg.wait_for_timeout(300)
                over=await pg.evaluate("(()=>{const r=document.querySelector('body > div');const kids=[...r.children].filter(c=>getComputedStyle(c).position!=='absolute');const last=kids[kids.length-1].getBoundingClientRect();return {bottom:Math.round(last.bottom),H:r.clientHeight,overflow:r.scrollHeight>r.clientHeight}})()")
                await pg.screenshot(path=fn+'.png')
                out.append((fn,over))
        for o in out: print(o)
        await b.close()
asyncio.run(main())
