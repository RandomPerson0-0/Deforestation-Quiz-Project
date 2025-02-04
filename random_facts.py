import random

list_of_random_facts = ["We Lose Around 10 Million Hectares of Forest Every "
                        "Single Year because The world has been "
                        "chopping down 10 million hectares of trees every year "
                        "to make space to grow crops and "
                        "livestock, and to produce materials such as paper.",
                        "Beef is Responsible for 41% of Global Deforestation "
                        "because The farming industry needs to "
                        "clear substantial pasture lands for cattle "
                        "(and livestock) in order to keep up with global "
                        "demand for beef. An estimated 81,081 square miles of "
                        "forest land is lost every year for meat "
                        "production, 80% of which occurs in the Amazon. ",
                        "Deforestation Contributes about 4.8 Billion Tonnes of "
                        "Carbon Dioxide A Year One of the most "
                        "stunning deforestation facts is that forest loss "
                        "contributes nearly 5 billion tons of carbon "
                        "dioxide into the atmosphere every year, which is "
                        "equivalent to nearly 10% of annual human "
                        "emissions. NASA researchers found that accelerated "
                        "slashing and burning methods of land "
                        "clearing in Borneo, the third-largest island in the"
                        "world and home to one of the oldest "
                        "rainforests in the world, contributed to the largest "
                        "single-year global increase in carbon "
                        "emissions in two millenniums, driving Indonesia up "
                        "towards a leading source of carbon "
                        "emissions. ",
                        "Brazil and Indonesia Account for Almost Half of "
                        "Tropical Deforestation That amounts to "
                        "approximately 1.7 million hectares each year. Both "
                        "Brazil and Indonesia are home to some of "
                        "the world’s largest and biodiversity tropical forests "
                        "in the world. As the agricultural "
                        "industry continues to practice land clearing for crop "
                        "and livestock farming, the threat to "
                        "biodiversity only worsens. Studies say observed "
                        "animal populations have experienced an "
                        "average 68% decline in population numbers. In Borneo, "
                        "Indonesia, the critically endangered "
                        "orangutan lost nearly 80% of its population within "
                        "the last 50 years. ",
                        "Soy Plays a Big Role in Deforestation While most "
                        "think of soy in the form of soy milk, "
                        "tofu and other soybean products that make up a "
                        "plant-based diet, soy in fact has been mostly "
                        "used as animal feed and to support the massive demand "
                        "of meat production. Animal feed makes "
                        "up 77% of soy production, while only 19.2% goes "
                        "directly into human food products. Globally, "
                        "soy is responsible for about 12% of deforestation. ",
                        "Deforestation Has Turned the Amazon Rainforest into a"
                        "Carbon Source One of the most shocking "
                        "deforestation facts in recent years is that the "
                        "Amazon, the world’s most biologically "
                        "diverse ecosystems and important carbon sinks, is "
                        "found to emit a greater amount of carbon "
                        "dioxide than it is absorbing as a result of "
                        "deforestation, wildfires and climate change. "
                        "According to a study between 2010 and 2018, "
                        "deforestation in eastern Amazonia has led to "
                        "greater warming and moisture stress to the forest "
                        "especially during dry seasons, "
                        "making it more susceptible to wildfires. ",
                        "More Than 100 Countries Have Pledged to End "
                        "Deforestation by 2030 Despite the current state "
                        "of deforestation, there is good news. At the recent "
                        "COP26 climate conference, a UN summit "
                        "for world leaders to conduct and negotiate policy "
                        "agreements on emissions reduction and "
                        "climate change mitigation, more than 100 countries "
                        "have joined a pledge to stop and reverse "
                        "deforestation by the end of the decade. Combined, "
                        "these 100+ countries make up 85% of the "
                        "world’s forests. Some of the most notable signatories "
                        "include Brazil, Russia, Colombia, "
                        "Indonesia and the Democratic Republic of the Congo. "
                        "The pact will see $19.2 billion of "
                        "private and public funds to help combat this global "
                        "environmental problem, from restoring "
                        "degraded land and supporting indigenous communities "
                        "to mitigating wildfire damage."]


# this function adds facts so when people are doing the quiz, they know some things about deforestation
def random_facts():
    random_deforestation = random.choice(list_of_random_facts)
    print("Did you know?", random_deforestation)

random_facts()