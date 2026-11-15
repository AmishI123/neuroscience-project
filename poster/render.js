const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:3456,height:2304},deviceScaleFactor:1});
await p.goto('file://'+process.argv[2]+'/poster.html');await p.waitForTimeout(500);
await p.pdf({path:process.argv[2]+'/poster.pdf',width:'36in',height:'24in',printBackground:true});
await p.screenshot({path:process.argv[2]+'/poster.png'});
const o=await p.evaluate(()=>[...document.querySelectorAll('.col')].map(c=>[c.scrollHeight,c.clientHeight]));console.log(JSON.stringify(o));await b.close()})();
