import random as ran
import info as i


# driver = webdriver.Firefox()
# driver.get('https://incorrect-quotes-generator.neocities.org/')


# prompt1 = driver.execute_script('return prompts1')
# prompt2 = driver.execute_script('return prompts2')
# prompt3 = driver.execute_script('return prompts3')

# prompt4 = driver.execute_script('return prompts4')
# prompt5 = driver.execute_script('return prompts5')
# prompt6 = driver.execute_script('return prompts6')

# prompt_list = [prompt1,prompt2,prompt3,prompt4,prompt5,prompt6]

# URL = "https://incorrect-quotes-tgenerator.neocities.org/"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# # soup.findall("script type="text/javascript"")
# # print(soup.prettify)
# # results =  re.search(r"var prompts1 = [(.*?)]", soup)
# results =  re.findall("var", soup.prettify)
# print(results)
# print(results)

# print(f'https:www.example.com/contact-us/{gaid}')

# pattern = re.compile("var prompts1 = \[(.*?)\];")
# test = pattern.findall(soup.text)
# print(test) 

new_list = []

for prompt_char in range(len(i.prompt_list)):
  new_sub_list = []
  for prompt in i.prompt_list[prompt_char]:
    new_prompt = prompt.replace("<br> ","\n")
    new_sub_list.append(new_prompt)
  new_list.append(new_sub_list)




def type_check(amount:int,*args):
  if len(args) != amount:
    return False
  if amount > 6 or amount < 1:
    return False 
  for ar in args:
    if type(ar) != str: 
      return False
  return True
  


def generate_prompt1(characters: int,name1:str):
    retval = new_list[0][ran.randint(0,len(new_list[0])-1)]
    retval = retval.replace("{A}",f'{name1}')
    return retval


def generate_prompt2(characters: int,name1:str,name2:str):
    retval = new_list[1][ran.randint(0,len(new_list[0])-1)]
    retval = retval.replace("{A}",f'{name1}')
    retval = retval.replace("{B}",f'{name2}')
    return retval

def generate_prompt3(characters: int,name1:str,name2:str,name3:str):
    retval = new_list[2][ran.randint(0,len(new_list[2])-1)]
    retval = retval.replace("{A}",f'{name1}')
    retval = retval.replace("{B}",f'{name2}')
    retval = retval.replace("{C}",f'{name3}')
    return retval


def generate_prompt4(characters: int,name1:str,name2:str,name3:str,name4:str):
    retval = new_list[3][ran.randint(0,len(new_list[3])-1)]
    retval = retval.replace("{A}",f'{name1}')
    retval = retval.replace("{B}",f'{name2}')
    retval = retval.replace("{C}",f'{name3}')
    retval = retval.replace("{D}",f'{name4}')
    return retval


def generate_prompt5(characters: int,name1:str,name2:str,name3:str,name4:str,name5:str):
    retval = new_list[4][ran.randint(0,len(new_list[4])-1)]
    retval = retval.replace("{A}",f'{name1}')
    retval = retval.replace("{B}",f'{name2}')
    retval = retval.replace("{C}",f'{name3}')
    retval = retval.replace("{D}",f'{name4}')
    retval = retval.replace("{E}",f'{name5}')
    return retval


def generate_prompt6(characters: int,name1:str,name2:str,name3:str,name4:str,name5:str,name6:str):
    retval = new_list[5][ran.randint(0,len(new_list[5])-1)]
    retval = retval.replace("{A}",f'{name1}')
    retval = retval.replace("{B}",f'{name2}')
    retval = retval.replace("{C}",f'{name3}')
    retval = retval.replace("{D}",f'{name4}')
    retval = retval.replace("{E}",f'{name5}')
    retval = retval.replace("{F}",f'{name6}')
    return retval


















