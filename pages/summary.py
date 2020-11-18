import streamlit as st
import numpy as np
import pandas as pd
from sum_functions import * 

text = '''For mountain lions living in Los Angeles—and yes, mountain lions do manage to survive in the second-largest city in the U.S.—the 101 freeway is a major barrier to their daily routines. The same is true for other wildlife. But plans to build a massive wildlife crossing over a 10-lane stretch of the freeway just north of the city are now in the final phase of design and engineering. The project will be the largest bridge of its kind in the world.
Reconnecting the open space on either side of the freeway is crucial for wildlife. “We know from science what’s going on there, and it’s a little deeper than just that the animals are getting hit by cars,” says Beth Pratt of the National Wildlife Federation, one of several partner organizations working on the project. “They are becoming genetically isolated, because animals cannot move into the small islands of habitat that are created by our freeways.” The situation is most acute for mountain lions, who risk extinction in the area within decades, but other wildlife, from lizards to birds, are also showing a decline in genetic diversity.
Fires fueled by climate change are making the challenges worse, as animals often can’t relocate when their habitat is destroyed, or they can’t directly flee the flames. A mountain lion named P-64, who died because of the Woolsey Fire, is one example. “That cat knew how to move in an urban environment,” Pratt says. “He had actually crossed the 101 using a culvert. But fire came and he could not get out of the burn zone.”
The project has been in planning for around eight years but is moving relatively quickly given the scale, complexity, and cost. “It’s over the busiest freeway, probably, in America, with multiple public agencies,” she says. “These things usually take decades. But I think everybody recognizes that mountain lions are running out of time.” The cost, at $87 million, will be largely funded by private money. If fundraising continues on schedule, the groundbreaking will happen in 2021.
Around the world, other wildlife crossings exist and have been proven to work, though the project will be the first in a dense urban area. “We have something no other crossing has, which is millions of people around it,” says Pratt. “The Kardashians are down the street. We’re building this in the most densely populated metropolitan area in the country, and these crossings, for the most part, have been built in very rural areas. So we have some things we have to mitigate for that they don’t, and two of those are sound and light.” Three hundred thousand to 400,000 cars pass through the area each day; the bridge, 165 feet wide, is designed to keep the crossing as quiet and dark as possible, with vegetation planted to extend to the wild spaces on either side of the freeway.
“We’re saving mountain lions, and we’re reconnecting an ecosystem for all wildlife,” she says. “But we’re also going to have some great model for what others can do in urban areas to get animals across the road.”'''


st.write("# Text Summarization")
st.write("Paste any news article into the following text field and get a short summary.") 

user_input_per = st.slider('How much should the text be reduced (%)?', min_value=0.1, max_value=0.9, value=0.9, step=0.05)

user_input_txt = st.text_area("Input for News Article:", text, height = 256)

if st.button("Generate summary"):
  get_summary(user_input_txt, (1-user_input_per))
  word_frequency(user_input_txt)