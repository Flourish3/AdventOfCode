package main

import org.scalatest.funsuite.AnyFunSuite


class Day01Test extends AnyFunSuite {
    val elves = Seq(Seq(1000, 2000, 3000), Seq(4000), Seq(5000, 6000), Seq(7000, 8000, 9000), Seq(10000))

    test("part 1") {
        assert(part1(elves) == 24000)
    }

    test("part 2") {
        assert(part2(elves) == 45000)
    }
}