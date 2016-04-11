%% -*- coding: UTF-8 -*-
-module(if1).
-export([heh_god/0, heh_god/1, score/1]).


%% test if
heh_god() ->
  if 1 =:= 1 ->
    work
  end,
  if 1 =:= 2; 1 =:= 1 ->
    work
  end,
  if 1 =:= 2, 1 =:= 1 ->  % Warning: no clause will ever match; the guard for this clause evaluates to 'false'
    fails
  end.


%% test if true
heh_god(X) ->
  if is_integer(X), X > 16, X < 104 -> good;
    true -> bad
  end,
  %if X == cat -> "cat";
  %   X == dog -> "dog";
  %   X == shit -> "shit";
  %   X == tree -> "tree";
  %   true -> wrong  % true is the else for if
  %end.
  X1 = [X|[X]],
  [12345|X1].


%% Score level
score(X) ->
 Score = if
   X >= 100 -> "A+";
   X >= 90  -> "A";
   X >= 80  -> "B";
   X >= 70  -> "C";
   X >= 60  -> "C-";
   true    -> "Failed"
 end,
 {"Your score level is: [" ++ Score ++ "]!", X}.
