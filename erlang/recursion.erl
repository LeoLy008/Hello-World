%% -*- coding: UTF-8 -*-
%% 20160413 recursion
%% reference:
-module(recursion).
-export([fact/1, tail_fact/1]).
-export([fib_seq/1, tail_fib_seq/1]).
-export([hanoi/4]).
-export([zip/2, tail_zip/2]).

%% ----------
%% factorial sequence
fact(1) -> 1;
fact(N) -> N*fact(N-1).

%% tail recursion factorial
tail_fact(1) -> 1;
tail_fact(N) -> tail_fact(N-1, N).

tail_fact(1, ACC) -> ACC;
tail_fact(N, ACC) ->
  io:format("tail_fact(~p, ~p)\n", [N, ACC]),
  tail_fact(N-1, ACC*N).



%% ----------
%% fibonacci sequence, common recursion version
fib_seq(1) -> 1;
fib_seq(2) -> 2;
fib_seq(N) ->
  A = fib_seq(N-2),
  B = fib_seq(N-1),
  io:format("~p, ~p, ~p\n", [A, B, A+B]),
  A + B.

%% tail recursion version of fibonacci sequence
tail_fib_seq(1) -> 1;
tail_fib_seq(2) -> 2;
tail_fib_seq(N) -> tail_fib_seq(N-1, 1, 2).

tail_fib_seq(2, ACC1, ACC2) -> ACC1+ACC2;
tail_fib_seq(N, ACC1, ACC2) ->
  io:format("tail_fib_seq(~p,~p,~p)\n", [N, ACC1, ACC2]),
  tail_fib_seq(N-1, ACC2, ACC1+ACC2).  %% 每次迭代，N减小， ACC1, ACC2 交替增加


%% ----------
%% 河内塔 Tower of Hanoi 问题
%% t1, t2, t3, n个珠子由小到大，（n, t1, t2, t3) 将N个珠子从t1 移动到 t3, t2 为临时塔
hanoi(1, T1, T2, T3) -> io:format("move 1 from ~p to ~p\n", [T1, T3]);
hanoi(N, T1, T2, T3) ->
  hanoi(N-1, T1, T3, T2),
  hanoi(1, T1, T2, T3),
  hanoi(N-1, T2, T1, T3).

%% tail Hanoi
%tail_hanoi(1, T1, T2, T3) -> io:format("move 1 from ~p to ~p\n", [T1, T3, T2]);
%tail_hanoi(N, T1, T2, T3) -> tail_hanoi(N-1, T1, T2, T3, ACC).

%tail_hanoi(2, T1, T2, T3, ACC) -> io:format("Unknown!!!\n", [T1, T2, T3, ACC]).


%% ----------
zip([],[]) -> [];
zip([X|Xs], [Y|Ys]) -> [{X,Y}|zip(Xs, Ys)].

%% tail version of zip
tail_zip(X, Y) -> tail_zip(X, Y, []).

tail_zip([], [], ACC) -> ACC;
tail_zip([X|Xs], [Y|Ys], ACC) -> tail_zip(Xs, Ys, [{X, Y}|ACC]).
