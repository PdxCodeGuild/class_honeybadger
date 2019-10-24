$_$wp(1);
var myName = ($_$w(1, 0), 'I.Williams');
var a = a || $_$w(1, 1);
$_$w(1, 2), $_$tracer.log(a, 'a', 1, 2);
var b = ($_$w(1, 3), 2);
$_$w(1, 4), a = 7;
$_$w(1, 5), $_$tracer.log(a, 'a', 1, 5);
$_$w(1, 6), b = a;
let myquote = ($_$w(1, 7), 'This is a "double" quote "string"');
$_$w(1, 8), $_$tracer.log(myquote, 'myquote', 1, 8);
let myquote2 = ($_$w(1, 9), `This is my "double"  'single double string' `);
$_$w(1, 10), $_$tracer.log(myquote2, 'myquote2', 1, 10);
let ourstring = ($_$w(1, 11), 'I come first ');
$_$w(1, 12), ourstring += 'I come second ';
$_$w(1, 13), $_$tracer.log(ourstring, 'ourstring', 1, 13);
let adj = ($_$w(1, 14), 'happy ');
let noun = ($_$w(1, 15), 'lawyer is ');
let verb = ($_$w(1, 16), 'running ');
$_$w(1, 17), article = 'the ';
$_$w(1, 18), combine = article += adj += noun += verb;
$_$w(1, 19), $_$tracer.log(combine, 'combine', 1, 19);
$_$w(1, 20), $_$tracer.log(ourstring.length, 'ourstring.length', 1, 20);
let lastname = ($_$w(1, 21), 'Lovelace');
$_$w(1, 22), $_$tracer.log(lastname.length, 'lastname.length', 1, 22);
$_$w(1, 23), $_$tracer.log(lastname[0], 'lastname[0]', 1, 23);
$_$w(1, 24), $_$tracer.log(lastname[2], 'lastname[2]', 1, 24);
$_$w(1, 25), $_$tracer.log(lastname[lastname.length - 1], 'lastname[lastname.length - 1]', 1, 25);
$_$w(1, 26), $_$tracer.log(lastname[lastname.length - 4], 'lastname[lastname.length - 4]', 1, 26);
$_$w(1, 27), $_$tracer.log(lastname[lastname.length - 3], 'lastname[lastname.length - 3]', 1, 27);
let myarray = ($_$w(1, 28), [
    50,
    20,
    78
]);
$_$w(1, 29), $_$tracer.log(myarray[1], 'myarray[1]', 1, 29);
$_$w(1, 30), myarray[0] = 29;
$_$w(1, 31), $_$tracer.log(myarray, 'myarray', 1, 31);
$_$w(1, 32), myNestedArray = [
    [
        1,
        2,
        3
    ],
    [
        4,
        5,
        6
    ],
    [
        7,
        8,
        9
    ],
    [
        [
            10,
            11,
            12
        ],
        13,
        14
    ]
];
$_$w(1, 33), $_$tracer.log(myNestedArray, 'myNestedArray', 1, 33);
$_$w(1, 34), $_$tracer.log(myNestedArray[0][0], 'myNestedArray[0][0]', 1, 34);
$_$w(1, 35), $_$tracer.log(myNestedArray[2][1], 'myNestedArray[2][1]', 1, 35);
$_$w(1, 36), $_$tracer.log(myNestedArray[3][0][2], 'myNestedArray[3][0][2]', 1, 36);
$_$w(1, 37), $_$tracer.log(myNestedArray[3][1], 'myNestedArray[3][1]', 1, 37);
$_$w(1, 38), array2 = [
    'simpson',
    'j',
    'cat'
];
$_$w(1, 39), array2.push([
    'liza',
    11
]);
$_$w(1, 40), $_$tracer.log(array2, 'array2', 1, 40);
$_$w(1, 41), removedFromArray = array2.pop();
$_$w(1, 42), $_$tracer.log(removedFromArray, 'removedFromArray', 1, 42);
$_$w(1, 43), $_$tracer.log(array2, 'array2', 1, 43);
$_$w(1, 44), array3 = [
    'bobcat',
    110,
    'kelly'
];
$_$w(1, 45), removeArray2 = array3.shift();
$_$w(1, 46), $_$tracer.log(removeArray2, 'removeArray2', 1, 46);
$_$w(1, 47), $_$tracer.log(array3, 'array3', 1, 47);
$_$w(1, 48), array3.unshift('Happy');
$_$w(1, 49), $_$tracer.log(array3, 'array3', 1, 49);
$_$w(1, 50), array3.unshift(['toto,45']);
$_$w(1, 51), $_$tracer.log(array3, 'array3', 1, 51);
function test() {
    $_$wf(1);
    $_$w(1, 52), $_$tracer.log('Holla, Holla', '', 1, 52);
}
;
$_$w(1, 53), test();
function add(a, b) {
    $_$wf(1);
    $_$w(1, 54), $_$tracer.log(a + b, 'a + b', 1, 54);
}
;
$_$w(1, 55), add(10, 12);
function mult5(num) {
    $_$wf(1);
    $_$w(1, 56), result = num * 5;
    return $_$w(1, 57), result;
}
;
$_$w(1, 58), times5 = mult5(7);
$_$w(1, 59), $_$tracer.log(times5, 'times5', 1, 59);
function nextInLine(arr, item) {
    $_$wf(1);
    let pushItem = ($_$w(1, 60), arr.push(item));
    let shiftItem = ($_$w(1, 61), arr.shift());
    return $_$w(1, 62), (pushItem, shiftItem);
    $_$w(1, 63), $_$wv(1, 63, '1,63', 'nextInLine', nextInLine, '$_$ne', 1, 0, '');
}
let nextArr = ($_$w(1, 64), [
    1,
    2,
    3,
    4,
    5
]);
let item = ($_$w(1, 65), 6);
let returnValue = ($_$w(1, 66), nextInLine(nextArr, item));
$_$w(1, 67), $_$tracer.log(returnValue, 'returnValue', 1, 67);
var testArr = ($_$w(1, 68), [
    1,
    2,
    3,
    4,
    5
]);
$_$w(1, 69), $_$tracer.log('Before: ' + JSON.stringify(testArr), '\'Before: \' + JSON.stringify(testArr)', 1, 69);
$_$w(1, 70), $_$tracer.log(nextInLine(testArr, 6), 'nextInLine(testArr, 6)', 1, 70);
$_$w(1, 71), $_$tracer.log('After: ' + JSON.stringify(testArr), '\'After: \' + JSON.stringify(testArr)', 1, 71);
function caseInSwith(val) {
    $_$wf(1);
    let answer = ($_$w(1, 72), '');
    switch ($_$w(1, 73), val) {
    case 1: {
            $_$w(1, 74), answer = 'alpha';
            {
                $_$w(1, 75);
                break;
            }
        }
    case 2: {
            $_$w(1, 76), answer = 'beta';
            {
                $_$w(1, 77);
                break;
            }
        }
    case 3: {
            $_$w(1, 78), answer = 'gamma';
            {
                $_$w(1, 79);
                break;
            }
        }
    case 4: {
            $_$w(1, 80), answer = 'delta';
            {
                $_$w(1, 81);
                break;
            }
        }
    default: {
            $_$w(1, 82), answer = 'not an option';
        }
    }
    return $_$w(1, 83), answer;
}
;
$_$w(1, 84), $_$tracer.log(caseInSwith(2), 'caseInSwith(2)', 1, 84);
function caseInSwith2(val) {
    $_$wf(1);
    let answer = ($_$w(1, 85), '');
    switch ($_$w(1, 86), val) {
    case 1:
    case 2:
    case 3: {
            $_$w(1, 87), answer = 'low';
            {
                $_$w(1, 88);
                break;
            }
        }
    case 4:
    case 5:
    case 6: {
            $_$w(1, 89), answer = 'mid';
            {
                $_$w(1, 90);
                break;
            }
        }
    case 7:
    case 8:
    case 9: {
            $_$w(1, 91), answer = 'high';
            {
                $_$w(1, 92);
                break;
            }
        }
    }
    return $_$w(1, 93), answer;
}
;
$_$w(1, 94), $_$tracer.log(caseInSwith2(5), 'caseInSwith2(5)', 1, 94);
function trueFalse(a, b) {
    $_$wf(1);
    return $_$w(1, 95), a < b;
}
$_$w(1, 96), $_$tracer.log(trueFalse(7, 8), 'trueFalse(7, 8)', 1, 96);
let testObj = ($_$w(1, 97), {
    'hat': 'ballcap',
    'shirt': 'jersey',
    'shoes': 'cleats'
});
let hatValue = ($_$w(1, 98), testObj.hat);
let shirtValue = ($_$w(1, 99), testObj.shirt);
$_$w(1, 100), $_$tracer.log(hatValue, shirtValue, 'hatValue', 1, 100);
let testObj2 = ($_$w(1, 101), {
    'my hat': 'ballcap',
    'her shirt': 'jersey',
    'his shoes': 'cleats'
});
let hisShoeValue = ($_$w(1, 102), testObj2['his shoes']);
let herShirtValue = ($_$w(1, 103), testObj2['her shirt']);
$_$w(1, 104), $_$tracer.log(hisShoeValue, herShirtValue, 'hisShoeValue', 1, 104);
let testObj3 = ($_$w(1, 105), {
    12: 'Namath',
    16: 'Montana',
    19: 'Unitas'
});
let playerNumber = ($_$w(1, 106), 16);
let player = ($_$w(1, 107), testObj3[playerNumber]);
$_$w(1, 108), $_$tracer.log(player, 'player', 1, 108);
let testObj4 = ($_$w(1, 109), {
    'Quarterback': 'Namath',
    'Goalie': 'Montana',
    'Center': 'Unitas'
});
$_$w(1, 110), testObj4.Quarterback = 'Mr. Namath';
$_$w(1, 111), $_$tracer.log(testObj4, 'testObj4', 1, 111);
$_$w(1, 112), testObj4['TightEnd'] = 'Jackson';
$_$w(1, 113), $_$tracer.log(testObj4, 'testObj4', 1, 113);
$_$w(1, 114), delete testObj4.Goalie;
$_$w(1, 115), $_$tracer.log(testObj4, 'testObj4', 1, 115);
function phoneticLookup(val) {
    $_$wf(1);
    let result = ($_$w(1, 116), '');
    var lookup = ($_$w(1, 117), {
        'alpha': 'Adams',
        'bravo': 'Boston',
        'charlie': 'Chicago',
        'delta': 'Denver',
        'echo': 'Easy',
        'foxtrot': 'Frank'
    });
    $_$w(1, 118), result = lookup[val];
    return $_$w(1, 119), result;
}
;
$_$w(1, 120), $_$tracer.log(phoneticLookup('foxtrot'), 'phoneticLookup(\'foxtrot\')', 1, 120);
let myobject = ($_$w(1, 121), {
    gift: 'Pony',
    pet: 'Kitten',
    bed: 'Sleigh'
});
function checkObj(checkProp) {
    $_$wf(1);
    if ($_$w(1, 122), myobject.hasOwnProperty(checkProp)) {
        return $_$w(1, 123), myobject[checkProp];
    } else {
        return $_$w(1, 124), 'Not Found';
    }
    ;
}
$_$w(1, 125), $_$tracer.log(checkObj('pet'), 'checkObj(\'pet\')', 1, 125);
let myMusic = ($_$w(1, 126), [{
        'artist': 'Billy Joel',
        'title': 'Piano Man',
        'release_year': 1973,
        'formats': [
            'cd',
            '8T',
            'lp'
        ],
        'gold': 'true'
    }]);
$_$w(1, 127), $_$tracer.log(myMusic, 'myMusic', 1, 127);
let myStorage = ($_$w(1, 128), {
    'car': {
        'inside': {
            'glove box': 'maps',
            'passenger seat': 'crumbs'
        },
        'outside': { 'trunk': 'jack' }
    }
});
let gloveBoxContents = ($_$w(1, 129), myStorage.car.inside['glove box']);
$_$w(1, 130), $_$tracer.log(gloveBoxContents, 'gloveBoxContents', 1, 130);
let trunkContents = ($_$w(1, 131), myStorage.car.outside.trunk);
$_$w(1, 132), $_$tracer.log(trunkContents, 'trunkContents', 1, 132);
let myPlants = ($_$w(1, 133), [
    {
        type: 'flowers',
        list: [
            'rose',
            'tulip',
            'dandelion'
        ]
    },
    {
        type: 'trees',
        list: [
            'firn',
            'pine',
            'birch'
        ]
    }
]);
let secondTree = ($_$w(1, 134), myPlants[1].list[1]);
$_$w(1, 135), $_$tracer.log(secondTree, 'secondTree', 1, 135);
$_$w(1, 136), $_$tracer.log(myPlants[0].list[2], 'myPlants[0].list[2]', 1, 136);
let myArray = ($_$w(1, 137), []);
let i = ($_$w(1, 138), 0);
while ($_$w(1, 139), i < 5) {
    $_$w(1, 140), myArray.push(i);
    $_$w(1, 141), ++i;
}
$_$w(1, 142), $_$tracer.log(myArray, 'myArray', 1, 142);
let ourArray = ($_$w(1, 143), []);
for (let i = 1; $_$w(1, 144), i < 6; i++) {
    $_$w(1, 145), ourArray.push(i);
}
$_$w(1, 146), $_$tracer.log(ourArray, 'ourArray', 1, 146);
let oddArray = ($_$w(1, 147), []);
for (let i = 1; $_$w(1, 148), i < 10; i += 2) {
    $_$w(1, 149), oddArray.push(i);
}
$_$w(1, 150), $_$tracer.log(oddArray, 'oddArray', 1, 150);
let backLoop = ($_$w(1, 151), []);
for (let i = 10; $_$w(1, 152), i > 0; i -= 2) {
    $_$w(1, 153), backLoop.push(i);
}
$_$w(1, 154), $_$tracer.log(backLoop, 'backLoop', 1, 154);
let backLoopOdd = ($_$w(1, 155), []);
for (let i = 9; $_$w(1, 156), i > 0; i -= 2) {
    $_$w(1, 157), backLoopOdd.push(i);
}
$_$w(1, 158), $_$tracer.log(backLoopOdd, 'backLoopOdd', 1, 158);
let myArray2 = ($_$w(1, 159), [
    9,
    10,
    11,
    12
]);
let myTotal = ($_$w(1, 160), 0);
for (let i = 0; $_$w(1, 161), i < myArray2.length; i++) {
    $_$w(1, 162), myTotal += myArray2[i];
}
;
$_$w(1, 163), $_$tracer.log(myTotal, 'myTotal', 1, 163);
function multiplyAll(arr) {
    $_$wf(1);
    let product = ($_$w(1, 164), 1);
    for (let i = 0; $_$w(1, 165), i < arr.length; ++i) {
        for (let j = 0; $_$w(1, 166), j < arr[i].length; ++j) {
            $_$w(1, 167), product *= arr[i][j];
        }
    }
    return $_$w(1, 168), product;
}
let product = ($_$w(1, 169), multiplyAll([
    [
        1,
        2
    ],
    [
        3,
        4
    ],
    [
        5,
        6,
        7
    ]
]));
$_$w(1, 170), $_$tracer.log(product, 'product', 1, 170);
$_$w(1, 171), myArray3 = [];
do {
    $_$w(1, 173), myArray3.push(i);
    $_$w(1, 174), i++;
} while ($_$w(1, 172), i < 5);
$_$w(1, 175), $_$tracer.log(myArray3, 'myArray3', 1, 175);
function randomFraction() {
    $_$wf(1);
    return $_$w(1, 176), Math.random();
}
;
$_$w(1, 177), $_$tracer.log(randomFraction(), 'randomFraction()', 1, 177);
let randomNumberBetween0and19 = ($_$w(1, 178), Math.floor(Math.random()) * 20);
function randomWholeNumber() {
    $_$wf(1);
    return $_$w(1, 179), Math.floor(Math.random() * 20);
}
;
$_$w(1, 180), $_$tracer.log(randomWholeNumber(), 'randomWholeNumber()', 1, 180);
function ourRandomRange(min, max) {
    $_$wf(1);
    return $_$w(1, 181), Math.floor(Math.random() * (max - min + 1) + min);
}
let myRandom = ($_$w(1, 182), ourRandomRange(1, 9));
$_$w(1, 183), $_$tracer.log(myRandom, 'myRandom', 1, 183);
function convertToInteger(str) {
    $_$wf(1);
    return $_$w(1, 184), parseInt(str);
}
$_$w(1, 185), convertToInteger('56');
function convertToInteger(str) {
    $_$wf(1);
    return $_$w(1, 186), parseInt(str, 2);
}
$_$w(1, 187), convertToInteger('10011');
function checkEqual(a, b) {
    $_$wf(1);
    if ($_$w(1, 188), a == b) {
        return $_$w(1, 189), true;
    } else {
        return $_$w(1, 190), false;
    }
}
function checkEqual(a, b) {
    $_$wf(1);
    return $_$w(1, 191), a === b ? ($_$w(1, 192), true) : ($_$w(1, 193), false);
    return $_$w(1, 194), a === b;
}
$_$w(1, 195), checkEqual(1, 4);
function checkSign(num) {
    $_$wf(1);
    return $_$w(1, 196), num > 0 ? ($_$w(1, 197), 'positive') : ($_$w(1, 198), num < 0 ? ($_$w(1, 199), 'negative') : ($_$w(1, 200), 'zero'));
}
$_$w(1, 201), $_$tracer.log(checkSign(0), 'checkSign(0)', 1, 201);
function checkScope() {
    'use strict';
    $_$wf(1);
    var i = ($_$w(1, 202), 'function scope');
    if ($_$w(1, 203), true) {
        let i = ($_$w(1, 204), 'block scope');
        $_$w(1, 205), $_$tracer.log('Block scope i is', i, '', 1, 205);
    }
    ;
    $_$w(1, 206), $_$tracer.log('Function scope i is ', i, '', 1, 206);
    return $_$w(1, 207), i;
}
$_$w(1, 208), checkScope();
function printManyTimes(str) {
    'use strict';
    $_$wf(1);
    const SENTENCE = ($_$w(1, 209), str + ' is cool');
    for (let i = 0; $_$w(1, 210), i < str.length; i += 2) {
        $_$w(1, 211), $_$tracer.log(SENTENCE, 'SENTENCE', 1, 211);
    }
}
$_$w(1, 212), printManyTimes('I.Williams');
const s = ($_$w(1, 213), [
    5,
    7,
    2
]);
function editPlace() {
    'use strict';
    $_$wf(1);
    $_$w(1, 214), s[0] = 2;
    $_$w(1, 215), s[1] = 5;
    $_$w(1, 216), s[2] = 7;
}
$_$w(1, 217), editPlace();
$_$w(1, 218), $_$tracer.log(s, 's', 1, 218);
function freezeObj() {
    'use strict';
    $_$wf(1);
    const Math_Constants = ($_$w(1, 219), { PI: 3.14 });
}
;
try {
    $_$w(1, 220), Math_Constants.PI = 99;
} catch (ex) {
    $_$w(1, 221), $_$tracer.log(ex, 'ex', 1, 221);
}
$_$wpe(1);