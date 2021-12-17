{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "02e1f18b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class User:\n",
    "    # аттрибуты класса\n",
    "    country = 'Russia'\n",
    "    \n",
    "    # константы принято писать капслоком\n",
    "    CITY = 'Moscow'\n",
    "    \n",
    "    # аттрибуты экземпляра\n",
    "    def __init__(self, name, surname, height, weight, rating=100):\n",
    "        self.surname = surname\n",
    "        self.name = name\n",
    "        self.rating = rating\n",
    "        \n",
    "        #приватный аттрибут к которому нельзя обратиться напрямую\n",
    "        self.__height = height\n",
    "        \n",
    "        # приватный аттрибут, к которому можно обратиться напрямую\n",
    "        self._weight = weight\n",
    "        \n",
    "    # метод класса\n",
    "    def decrease_rating(self, value):\n",
    "        self.rating -= value\n",
    "        \n",
    "    # свойства класса прописываются с помощью декоратора @property\n",
    "    \n",
    "    @property\n",
    "    def height(self):\n",
    "        return self.__height\n",
    "    \n",
    "    @property\n",
    "    def weight(self):\n",
    "        return self._weight\n",
    "    \n",
    "    @weight.setter\n",
    "    def weight(self, weight):\n",
    "        if weight > 80:\n",
    "            self._weight = 80\n",
    "        else:\n",
    "            self._weight = weight\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "715c11de",
   "metadata": {},
   "outputs": [],
   "source": [
    "user = User('Ivan', 'Manko', 170, 75)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "4669fb08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.User at 0x7fb0f8da9730>"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "3cd241ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Manko'"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user.surname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "2db0a231",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Russia'"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "User.country"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "84cde537",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 181,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user.rating"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "e04a7ad0",
   "metadata": {},
   "outputs": [],
   "source": [
    "user.decrease_rating(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "f0de1995",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "70"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user.rating"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "c719ade4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "170"
      ]
     },
     "execution_count": 184,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Вызов приватного аттрибута экзепляра\n",
    "user._User__height"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "50126d87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "75"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user._weight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "5a0e64a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "75"
      ]
     },
     "execution_count": 186,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# вызываем свойства класса\n",
    "user.weight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "d1aed369",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "170"
      ]
     },
     "execution_count": 187,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user.height"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "92c497fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# назначая значение этому свойству, мы получаем значение соответствующее логике которую мы прописали \n",
    "user.weight = 65"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "e6a53f19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "65"
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user.weight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "d1bb7186",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Date:\n",
    "    def __init__(self, month, day, year):\n",
    "        self.month = month\n",
    "        self.day = day\n",
    "        self.year = year\n",
    "    \n",
    "    def display(self):\n",
    "        return f\"{self.day}/{self.month}/{self.year}\"\n",
    "    \n",
    "    # несет информацию о классе\n",
    "    @classmethod\n",
    "    def milleneum(cls, month, day):\n",
    "        return cls(month, day, 2000)\n",
    "    \n",
    "    #Статистический метод абстрагирован от класса.\n",
    "    @staticmethod\n",
    "    def milleneum_static(month, day):\n",
    "        return Date(month, day, 2000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "da4e0d06",
   "metadata": {},
   "outputs": [],
   "source": [
    "d1 = Date.milleneum(10,23)\n",
    "d2 = Date.milleneum_static(10,23)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "id": "ed3fb5ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'23/10/2000'"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.display()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "id": "cdfd6385",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'23/10/2000'"
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1322e1c",
   "metadata": {},
   "source": [
    "НАСЛЕДОВАНИЕ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "id": "8480cbd9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Shape:\n",
    "    def __init__(self):\n",
    "        print(\"Shape's created\")\n",
    "        \n",
    "    def draw(self):\n",
    "        print(\"shape is drawing\")\n",
    "        \n",
    "    def area(self):\n",
    "        print(\"calc area\")\n",
    "        \n",
    "    def perimeter(self):\n",
    "        print(\"calc perimeter\")\n",
    "        \n",
    "    def not_inplemented_method(self):\n",
    "        raise NotImplementedError(\"Нельзя наследовать этот метод\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "id": "4a07b6c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Rectangle(Shape):\n",
    "    def __init__(self, width, height):\n",
    "        Shape.__init__(self)\n",
    "        self.width = width\n",
    "        self.height = height\n",
    "        \n",
    "        \n",
    "    # Методы можно переопределять\n",
    "    def area(self):\n",
    "        return self.width * self.height\n",
    "        \n",
    "        print(\"Rectangle created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "id": "6a0f7318",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape's created\n"
     ]
    }
   ],
   "source": [
    "rec = Rectangle(10, 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "b9b334d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "calc perimeter\n"
     ]
    }
   ],
   "source": [
    "rec.perimeter()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "id": "8e675e36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 211,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rec.area()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "4572f1f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "class Triangle(Shape):\n",
    "    def __init__(self, a, b, c):\n",
    "        Shape.__init__(self)\n",
    "        self.a = a\n",
    "        self.b = b\n",
    "        self.c = c\n",
    "        print(\"triangle created\")\n",
    "        \n",
    "    def draw(self):\n",
    "        print(\"drawing triangle\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "b24f653f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape's created\n",
      "triangle created\n"
     ]
    }
   ],
   "source": [
    "tr = Triangle(1,2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "id": "2a78c91c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NotImplementedError",
     "evalue": "Нельзя наследовать этот метод",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNotImplementedError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_5731/3567294093.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnot_inplemented_method\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/tmp/ipykernel_5731/2680030329.py\u001b[0m in \u001b[0;36mnot_inplemented_method\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mnot_inplemented_method\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mNotImplementedError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Нельзя наследовать этот метод\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNotImplementedError\u001b[0m: Нельзя наследовать этот метод"
     ]
    }
   ],
   "source": [
    "tr.not_inplemented_method()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9031d161",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
