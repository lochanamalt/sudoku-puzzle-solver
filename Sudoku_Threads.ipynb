{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import threading\n",
    "import concurrent.futures"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = np.loadtxt(\"puzzle.txt\", dtype=np.int16)\n",
    "emptycells=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#finding empty cells and append them to the array\n",
    "for row in range(9): \n",
    "    for col in range(9): \n",
    "        if(data[row][col]==0): \n",
    "            emptycells.append([row,col])\n",
    "\n",
    "#print grid\n",
    "def grid(arr): \n",
    "    for i in range(9): \n",
    "        for j in range(9): \n",
    "            print(arr[i][j], end = ' ')\n",
    "        print() \n",
    "        \n",
    "def check_possibility_in_row(arr,row,num):\n",
    "    for i in range(9):\n",
    "        if(arr[row][i] == num):\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def check_possibility_in_col(arr,col,num):\n",
    "    for i in range(9):\n",
    "        if(arr[i][col] == num):\n",
    "            return False\n",
    "    return True\n",
    "        \n",
    "def check_possibility_in_subsquare(arr,row,col,num):\n",
    "    if((row+1)%3== 0):\n",
    "        row = row - 2\n",
    "    else:\n",
    "        row = row + 1 - (row+1)%3\n",
    "        \n",
    "    if((col+1)%3== 0):\n",
    "        col = col - 2  \n",
    "    else:\n",
    "        col = col + 1 - (col+1)%3  \n",
    "        \n",
    "    for i in range(3): \n",
    "        for j in range(3): \n",
    "            if(arr[i+row][j+col] == num):\n",
    "                return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "i=0\n",
    "start_value = 1\n",
    "filled = 0\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    while(i<len(emptycells)):\n",
    "        row = emptycells[i][0]\n",
    "        col = emptycells[i][1] \n",
    "        for num in range(start_value,10):\n",
    "\n",
    "            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:\n",
    "                possibility_col = executor.submit(check_possibility_in_col, data,col,num).result()\n",
    "                possibility_row = executor.submit(check_possibility_in_row, data,row,num).result()\n",
    "                possibility_subsquare = executor.submit(check_possibility_in_subsquare, data,row,col,num).result()\n",
    "\n",
    "            if(possibility_row and possibility_col and possibility_subsquare):\n",
    "                data[row][col] = num\n",
    "                start_value = 1\n",
    "                filled = 1\n",
    "                break\n",
    "\n",
    "        if(filled == 0):\n",
    "            i = i-1\n",
    "            row = emptycells[i][0]\n",
    "            col = emptycells[i][1]        \n",
    "            start_value = data[row][col] + 1\n",
    "            data[row][col] = 0\n",
    "        else:\n",
    "            i = i+1\n",
    "            filled = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 1 6 5 7 8 4 9 2 \n",
      "5 2 9 1 3 4 7 6 8 \n",
      "4 8 7 6 2 9 5 3 1 \n",
      "2 6 3 4 1 5 9 8 7 \n",
      "9 7 4 8 6 3 1 2 5 \n",
      "8 5 1 7 9 2 6 4 3 \n",
      "1 3 8 9 4 7 2 5 6 \n",
      "6 9 2 3 5 1 8 7 4 \n",
      "7 4 5 2 8 6 3 1 9 \n"
     ]
    }
   ],
   "source": [
    "grid(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
