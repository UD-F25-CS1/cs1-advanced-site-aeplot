from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

from meta import *
from state import State

messages = [
    '''You need help with your computer science project.''',
    '''Oh no! Your cactus looks unhappy, and you're not sure what to do.''',
    '''''',
    '''''',
]

@route
def index(state: State) -> Page:
    return Page(state, [
        Header('⚡️ Energy Simulator ⚡️',4),
        Button('''Start''',url = '/main_game'),
        Button('''Wait, I'm not ready yet!''', url = '/ready_or_not'),
        Button('''About''',url='/about'),
    ])

@route
def ready_or_not(state:State):
    return Page(state, [
        '''We're already in this world and using energy... play to get more ready.''',
        '''Or you can go read the about page.''',
        Button('''Start''',url = '/main_game'),
        Button('''About''',url='/about'),
    ])

@route
def about(state:State):
    return Page(state, [
        Header('⚡️ About ⚡️',4),
        '''This game is centered around AI and internet use and the environmental impacts of when we use it./n
        If we can spread awareness about these impacts, maybe then we can come together to take action as a whole.''',

        'Resources:',
        'https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117',
        'https://www.weforum.org/stories/2025/06/how-ai-use-impacts-the-environment/',
        'https://www.weforum.org/stories/2025/01/artificial-intelligence-climate-transition-drive-growth/',
        'https://www.nea.org/professional-excellence/student-engagement/tools-tips/environmental-impact-ai',

        Button('Back','/index')
    ])

@route
def main_game(state:State):
    return Page(state, [
        messages[state.count],
        Button('Ask AI','/ai_points'),
        Button('Surf the web','/web_points'),
        Button('Ask a friend','/friend_points')
    ])

@route
def ai_points(state:State):
    state.energy_used += 5
    state.count += 1
    if state.count >= 4:
        return check_points(state)
    else:
        return main_game(state)

@route
def web_points(state:State):
    state.energy_used += 1
    state.count += 1
    if state.count >= 4:
        return check_points(state)
    else:
        return main_game(state)

@route
def friend_points(state:State):
    state.count += 1
    if state.count >= 4:
        return check_points(state)
    else:
        return main_game(state)


def check_points(state:State):
    if state.energy_used >= 11:
        return high_energy_ending(state)
    elif state.energy_used >= 6:
        return mid_energy_ending(state)
    else:
        return lower_energy_ending(state)
    
def high_energy_ending(state:State):
    return Page(state, [
        Header('⚡️ Energy Simulator ⚡️',4),
        'You used', str(state.energy_used), 'units of energy.',
        '''That's a lot!''',
        'Your cactus is unhappy. It can see into the future.'
        'It seems to want you to do something.',
        'The highest contributing factor was: AI Usage.',
        Button('Play Again','index'),
    ])

def mid_energy_ending(state:State):
    return Page(state, [
        Header('⚡️ Energy Simulator ⚡️',4),
        'You used', str(state.energy_used), 'units of energy.',
        '''That's a significant amount.''',
        'Your cactus is looking moderately unhappy. It can see into the future.',
        'It seems to want you to do something.',
        Button('Play Again','index'),
    ])

def lower_energy_ending(state:State):
    return Page(state, [
        Header('⚡️ Energy Simulator ⚡️',4),
        'You used a few units of energy.',
        '''That's a little, but not truly zero.''',
        '''Even if you don't choose to use as much energy through AI use and the internet, others are still using it more.''',
        'Your cactus is slightly unhappy. It can see into the future.',
        'It seems to want you to do something.',
        Button('Play Again','index'),
    ])

start_server(State(energy_used=0,count=0),port=8080)
