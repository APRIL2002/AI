
% Facts
male(atmaram).
male(deepak).
male(ashok).
male(krunal).
male(smit).
male(akash).
female(savita).
female(brinda).
female(kailash).
female(nidhi).
female(priya).

parent(atmaram, deepak).
parent(atmaram, ashok).
parent(atmaram, priya).
parent(savita, priya).
parent(savita, deepak).
parent(savita, ashok).
parent(deepak, krunal).
parent(deepak, smit).
parent(brinda, krunal).
parent(brinda, smit).
parent(ashok, akash).
parent(ashok, nidhi).
parent(kailash, akash).
parent(kailash, nidhi).

% Rules
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
hasChild(X) :- parent(X,Y).
brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y), X \= Y.
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y), X \= Y.
grandfather(X, Y) :- male(X), parent(X, Z), parent(Z, Y).
grandmother(X, Y) :- female(X), parent(X, Z), parent(Z, Y).
uncle(X, Y) :- male(X), brother(X, Z), parent(Z, Y).
aunt(X, Y) :- female(X), sister(X, Z), parent(Z, Y).
