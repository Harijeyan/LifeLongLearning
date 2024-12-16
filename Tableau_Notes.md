## 5 Calculations for Year-over-Year Sales Difference

| Calculation | Formula |
|---|---|
| Current Year | {MAX(YEAR([Order Date]))} |
| Prior Year | [Current Year] - 1 |
| CY Sales | IF [Current Year] = YEAR([Order Date]) THEN [Sales] END |
| PY Sales | IF [Prior Year] = YEAR([Order Date]) THEN [Sales] END |
| CY vs PY | (SUM([CY Sales]) - SUM([PY Sales])) / SUM([PY Sales]) |

## Date Calculations Cheat sheet

<div class='tableauPlaceholder' id='viz1734367060733' style='position: relative'><noscript><a href='#'><img alt='Cheat Sheet ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;DateCalculationsCheatSheet&#47;CheatSheet&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DateCalculationsCheatSheet&#47;CheatSheet' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;DateCalculationsCheatSheet&#47;CheatSheet&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='_gl=1*1pnsva7*_ga*NDUxNjM4OTY0LjE3MjA2NzI1OTU.*_ga_8YLN0SNXVS*MTczNDM2NjkzNS4xMDAuMC4xNzM0MzY2OTM1LjAuMC4w' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1734367060733');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='777px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
