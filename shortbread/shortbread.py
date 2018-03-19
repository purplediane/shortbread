# -*- coding: utf-8 -*-

"""Main module."""
import inflect

p = inflect.engine()


def integerize(num, count):
    """Calculate and return integer value if result is integer"""
    calc = num * count
    calc = int(calc) if calc.is_integer() else calc
    return calc


def shortbread(count, long_list=False, choc=False):
    """Prints ingredients for making `count` dozen shortbread cookies."""
    title = 'Shortbread'
    if choc:
        title = 'Chocolate Chip Shortbread'
    title += ' Cookies - makes approx. {} doz.'.format(count)
    quarter = integerize(.25, count)
    half = integerize(.5, count)
    print(title)
    print('{} {} flour'.format(count, p.plural('cup', count)))
    print('{} {} sugar (may use brown sugar)'.format(quarter,
          p.plural('cup', quarter)))
    print('{} {} salted butter (NOT margarine), softened'.format(half,
          p.plural('cup', half)))
    print('{} {} vanilla (optional)'.format(quarter,
          p.plural('teaspoon', quarter)))
    if choc:
        print('{} {} baking powder'.format(quarter,
              p.plural('teaspoon', quarter)))
        print('{} {} small semisweet chocolate chips'.format(quarter,
              p.plural('cup', quarter)))
    light = 15 if choc else 10
    dark = 20 if choc else 12
    baking = '- Bake {} to {} minutes at 350 '.format(light, dark)
    baking += 'degrees until golden brown.'
    baking_hint = 'Bake cookies at 350 degrees for '
    baking_hint += '{}-{} minutes'.format(light, dark)

    if not long_list:
        print(baking_hint)
        return
    print()
    print('- Preheat oven to 350 degrees F.')
    print('- Cream the butter and sugar together well.')
    print('- Stir in optional vanilla.')
    if choc:
        print('- Sift together baking powder and flour.')
    print('- Mix in the flour until it makes a stiff dough.')
    print('- Add a bit more flour if dough is too soft.')
    if choc:
        print('- Stir in the chocolate chips.')
        print('- Scoop and roll into walnut-sized balls.')
    else:
        print('- Roll out 1/4 to 1/2 inch thick and cut into cookies.')
    print('- Place on baking sheet; line with parchment paper if desired.')
    if choc:
        print('- Flatten cookie balls slightly.')
    print(baking)
    print('When cool, enjoy your delicious cookies!')
