import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    X, Y, Z = map(int, readline().split())

    collision_time = X / (2*Y)
    fly_distance = int(collision_time * Z)

    write(str(fly_distance))
