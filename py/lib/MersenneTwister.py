# from _typeshed import Self
from typing import List
import time
from math import floor

double = float

_int = int


class uint(_int):
    def __new__(cls, value):
        return value & 0xFFFFFFFF


class MersenneTwister:
    # Class MersenneTwister generates random numbers
    # from a uniform distribution using the Mersenne
    # Twister algorithm.
    N: int = 624
    M: int = 397
    MATRIX_A: uint = 0x9908B0DF
    UPPER_MASK: uint = 0x80000000
    LOWER_MASK: uint = 0x7FFFFFFF
    MAX_RAND_INT: int = 0x7FFFFFFF
    mag01: List[uint] = [0x0, MATRIX_A]
    mt: List[uint] = [0] * N
    mti: int = N + 1

    def __init__(self, seed: int = None) -> None:
        if seed == None:
            seed = time.timens()
        self.init_genrand(uint(seed))

    # public MersenneTwister(int[] init)
    # {
    #     uint[] initArray = new uint[init.Length];
    #     for (int i = 0; i < init.Length; ++i)
    #         initArray[i] = (uint)init[i];
    #     init_by_array(initArray, (uint)initArray.Length);
    # }
    MaxRandomInt: int = 0x7FFFFFFF

    def Next(self, minValue: int = None, maxValue: int = None) -> int:
        if minValue == None:
            if maxValue == None:
                return self.genrand_int31()
            minValue = 0

        if minValue > maxValue:
            minValue, maxValue = maxValue, minValue
        return int(floor((maxValue - minValue + 1) * self.genrand_real1() + minValue))

    def NextFloat(self, includeOne: bool = False) -> float:
        if includeOne:
            return float(self.genrand_real1())
        return float(self.genrand_real2())

    def NextFloatPositive(self) -> float:
        return float(self.genrand_real3())

    def NextDouble(self, includeOne: bool = False) -> double:
        if includeOne:
            return self.genrand_real(1)
        return self.genrand_real2()

    def NextDoublePositive(self) -> double:
        return self.genrand_real3()

    def Next53BitRes(self):
        return self.genrand_res53()

    def NextBytes(self, length: int) -> bytes:
        return b"".join(
            self.genrand_int31().to_bytes(4, "little", signed=False)
            for _ in range(0, length, 4)
        )[:length]

    # public void Initialize()
    # { init_genrand((uint)DateTime.Now.Millisecond); }
    # public void Initialize(int seed)
    # { init_genrand((uint)seed); }
    # public void Initialize(int[] init)
    # {
    #     uint[] initArray = new uint[init.Length];
    #     for (int i = 0; i < init.Length; ++i)
    #         initArray[i] = (uint)init[i];
    #     init_by_array(initArray, (uint)initArray.Length);
    # }
    def init_genrand(self, s: uint) -> None:
        self.mt[0] = s & 0xFFFFFFFF
        for mti in range(1, self.N):
            self.mt[mti] = (
                uint(1812433253 * (self.mt[mti - 1] ^ (self.mt[mti - 1] >> 30)) + mti)
                & 0xFFFFFFFF
            )
        self.mti = self.N

    # private void init_by_array(uint[] init_key, uint key_length)
    # {
    #     int i, j, k;
    #     init_genrand(19650218U);
    #     i = 1; j = 0;
    #     k = (int)(N > key_length ? N : key_length);
    #     for (; k > 0; k--)
    #     {
    #         mt[i] = (uint)((uint)(mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) * 1664525U)) + init_key[j] + j);
    #         mt[i] &= 0xffffffffU;
    #         i++; j++;
    #         if (i >= N) { mt[0] = mt[N - 1]; i = 1; }
    #         if (j >= key_length) j = 0;
    #     }
    #     for (k = N - 1; k > 0; k--)
    #     {
    #         mt[i] = (uint)((uint)(mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) *
    #         1566083941U)) - i);
    #         mt[i] &= 0xffffffffU;
    #         i++;
    #         if (i >= N) { mt[0] = mt[N - 1]; i = 1; }
    #     }
    #     mt[0] = 0x80000000U;
    # }

    def genrand_int32(self) -> uint:
        y: uint
        if self.mti >= self.N:
            kk: int
            if self.mti == self.N + 1:
                self.init_genrand(5489)
            for kk in range(self.N - self.M):
                y = uint(
                    (self.mt[kk] & self.UPPER_MASK)
                    | (self.mt[kk + 1] & self.LOWER_MASK)
                )
                self.mt[kk] = uint(
                    self.mt[kk + self.M] ^ (y >> 1) ^ self.mag01[y & 0x1]
                )
            for kk in range(self.N - self.M, self.N - 1):
                y = uint(
                    (self.mt[kk] & self.UPPER_MASK)
                    | (self.mt[kk + 1] & self.LOWER_MASK)
                )
                self.mt[kk] = uint(
                    self.mt[kk + (self.M - self.N)] ^ (y >> 1) ^ self.mag01[y & 0x1]
                )

            y = uint(
                (self.mt[self.N - 1] & self.UPPER_MASK) | (self.mt[0] & self.LOWER_MASK)
            )
            self.mt[self.N - 1] = uint(
                self.mt[self.M - 1] ^ (y >> 1) ^ self.mag01[y & 0x1]
            )
            self.mti = 0

        y = self.mt[self.mti]
        self.mti += 1
        y = uint(y ^ (y >> 11))
        y = uint(y ^ ((y << 7) & 0x9D2C5680))
        y = uint(y ^ ((y << 15) & 0xEFC60000))
        y = uint(y ^ (y >> 18))
        return y

    def genrand_int31(self) -> int:
        return int(self.genrand_int32() >> 1)

    def genrand_real1(self) -> double:
        return self.genrand_int32() * (1.0 / 4294967295.0)

    def genrand_real2(self) -> double:
        return self.genrand_int32() * (1.0 / 4294967296.0)

    def genrand_real3(self) -> double:
        return (double(self.genrand_int32()) + 0.5) * (1.0 / 4294967296.0)

    def genrand_res53(self):
        a = uint(self.genrand_int32() >> 5)
        b = uint(self.genrand_int32() >> 6)
        return (a * 67108864.0 + b) * (1.0 / 9007199254740992.0)
