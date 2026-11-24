import json,html
LOGO="/_blob/1195e0fa49338d91f8364d3ed921bb53"
ICON={
'check':'<path d="M4 12.5l5 5L20 6.5"></path>',
'x':'<path d="M6 6l12 12M18 6L6 18"></path>',
}
P={'purple':'#8C28E9','green':'#33FF12','yellow':'#F9CC15'}
LIGHT={'purple':'#B57BFF','green':'#5CFF3F','yellow':'#F9CC15'}
ORDER=['purple','green','yellow']
def poster(d,W=1080,H=1350):
    lead=d.get('lead','purple'); i=ORDER.index(lead); second=ORDER[(i+1)%3]; third=ORDER[(i+2)%3]
    ctaBg=P[lead]; ctaFg='#ffffff' if lead=='purple' else '#0a0a0a'
    hl=LIGHT[lead]; eb=LIGHT[second]; ic=P[third] if third!='purple' else LIGHT['purple']
    eyebrow,h1a,h1b,body,items,icon,cta1,tag=d['eyebrow'],d['h1a'],d['h1b'],d['body'],d['items'],d.get('icon','check'),d.get('cta','Tell us what you need'),d.get('tag','We build it. We host it. We look after it.')
    col = ic if icon=='check' else '#F9CC15'
    cols = d.get('cols',2)
    svg=f'<svg aria-hidden="true" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{ICON[icon]}</svg>'
    chips="\n".join(f'<div style="display: flex; align-items: center; gap: 14px; background: #17131F; border: 1px solid {P[third]}55; border-radius: 14px; padding: 20px 22px">{svg}<span style="font-size: {d.get("chipSize",26)}px; font-weight: 600">{html.escape(t)}</span></div>' for t in items)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(d['title'])}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:#C9A0FF}}a:hover{{color:#ffffff}}
</style>
</helmet>
<div style="width: {W}px; height: {H}px; box-sizing: border-box; background: #0a0a0a; position: relative; overflow: hidden; font-family: Inter, system-ui, sans-serif; color: #F4F2F7; padding: 64px 72px; display: flex; flex-direction: column; gap: 34px">
<div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: {W}px; height: 16px; display: flex"><div style="flex: 1; background: #8C28E9"></div><div style="flex: 1; background: #33FF12"></div><div style="flex: 1; background: #F9CC15"></div></div>
<div aria-hidden="true" style="position: absolute; left: 0; bottom: 0; width: {W}px; height: 16px; display: flex"><div style="flex: 1; background: #F9CC15"></div><div style="flex: 1; background: #33FF12"></div><div style="flex: 1; background: #8C28E9"></div></div>
<div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 16px; height: {H}px; background: #33FF12"></div>
<div aria-hidden="true" style="position: absolute; right: 0; top: 0; width: 16px; height: {H}px; background: #F9CC15"></div>
<div aria-hidden="true" style="position: absolute; right: -240px; top: -200px; width: 680px; height: 680px; border-radius: 50%; border: 2px solid {P[second]}55"></div>
<div aria-hidden="true" style="position: absolute; right: -130px; top: -90px; width: 460px; height: 460px; border-radius: 50%; border: 2px solid {P[third]}40"></div>

<div style="display: flex; align-items: center; gap: 22px; position: relative">
<img src="{LOGO}" alt="TLC Talent Learn Consult logo" style="width: 96px; height: 96px; border-radius: 12px">
<div style="display: flex; flex-direction: column; gap: 4px">
<div style="font-family: Syne, sans-serif; font-weight: 700; font-size: 28px; letter-spacing: 0.5px">Talent Learn Consult</div>
<div style="font-size: 21px; color: #B9B3C4">{html.escape(tag)}</div>
</div>
</div>

<div style="display: flex; flex-direction: column; gap: 20px; position: relative">
<div style="font-size: 22px; font-weight: 600; letter-spacing: 3px; color: {eb}; text-transform: uppercase">{html.escape(eyebrow)}</div>
<h1 style="margin: 0; font-family: Syne, sans-serif; font-weight: 800; font-size: {d.get('h1Size',74)}px; line-height: 1.04; letter-spacing: -1px">{html.escape(h1a)} <span style="color: {hl}">{html.escape(h1b)}</span></h1>
<p style="margin: 0; font-size: 30px; line-height: 1.4; color: #D8D3E0">{html.escape(body)}</p>
</div>

<div style="display: grid; grid-template-columns: {' '.join(['1fr']*cols)}; gap: 14px; position: relative">
{chips}
</div>

<div style="margin-top: auto; display: flex; flex-direction: column; gap: 16px; position: relative">
<div style="background: {ctaBg}; border-radius: 20px; padding: 28px 34px; display: flex; align-items: center; justify-content: space-between; gap: 24px">
<div style="display: flex; flex-direction: column; gap: 6px">
<div style="font-family: Syne, sans-serif; font-weight: 800; font-size: 38px; color: {ctaFg}">{html.escape(cta1)}</div>
<div style="font-size: 27px; font-weight: 600; color: {ctaFg}">talentlearnconsult.com/website</div>
</div>
<svg aria-hidden="true" width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="{ctaFg}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
<div style="display: flex; justify-content: space-between; font-size: 23px; color: #D8D3E0">
<span>{{{{ footerLeft }}}}</span>
<span>WhatsApp 064 224 9229</span>
</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"footerLeft":{{"editor":"text","default":"Link in bio"}},"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{ footerLeft: this.props.footerLeft ?? 'Link in bio' }};
}}
}}
</script>
</body>
</html>
'''
days=[
dict(lead='green',file='Day2-NewBusiness.dc.html',title='Day 2 · Thu 26 Nov · Just registered',eyebrow='Just registered your business?',h1a='Get online the right way,',h1b='from day one.',body='New businesses get one chance at a first impression. We set up everything you need to look professional and get found.',items=['Your own domain name','Business email addresses','A website that works on phones','WhatsApp chat built in','Found on Google','Hosting and support'],cta='Start with a website'),
dict(lead='yellow',file='Day3-AEO.dc.html',title='Day 3 · Fri 27 Nov · AI search',eyebrow='The new way people search',h1a='Customers now ask AI who to call.',h1b='Will it name you?',body='More people ask AI assistants for recommendations. AEO (answer engine optimisation) helps your business show up in those answers, not just on Google.',items=['AEO: found in AI answers','SEO: found on Google','Clear, trusted business info','Analytics to see what works'],cols=1,h1Size=70),
dict(lead='purple',file='Day4-Email.dc.html',title='Day 4 · Sat 28 Nov · Business email',eyebrow='Quick question',h1a='Still using a Gmail address',h1b='for your business?',body='An email address with your own business name builds trust before you even say hello.',items=['you@yourbusiness.co.za','Set up on your phone and PC','Matches your domain and website','Looked after by us'],cols=1,cta='Get your business email'),
dict(lead='green',file='Day5-Proof.dc.html',title='Day 5 · Sun 29 Nov · Our work',eyebrow='Real businesses. Real websites.',h1a='Built by TLC,',h1b='working for our clients.',body='From appliance repairs to logistics to a church community, we build websites that fit the business.',items=['B A Appliances Spares and Repairs','Skosana JR Logistics','RCA Charisma'],cols=1,cta='Yours could be next'),
dict(lead='yellow',file='Day6-Signs.dc.html',title='Day 6 · Mon 30 Nov · Warning signs',eyebrow='3 signs your website is losing you customers',h1a='Is your website',h1b='sending customers away?',body='If any of these sound familiar, it is time for a fix.',items=['It is slow or messy on a phone','Customers cannot easily contact you','Your info, prices or photos are out of date'],icon='x',cols=1,cta='Let us take a look'),
dict(lead='purple',file='Day7-Care.dc.html',title='Day 7 · Tue 1 Dec · Website care',eyebrow='After your website goes live',h1a='Who looks after your website',h1b='when something breaks?',body='A website is not a once-off job. We keep yours healthy, up to date and working, so you never have to chase anyone.',items=['Website health checks','Maintenance and updates','Hosting and domain renewals','Business email support','Analytics','One number to call'],cta='Get looked after'),
]
import os
os.chdir('/home/claude/poster/project')
for d in days: open(d['file'],'w').write(poster(d))
json.dump([d['file'] for d in days],open('/home/claude/gen/files.json','w'))
print('ok')
