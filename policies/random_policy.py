from gym_duckiematrix.DB21J import DuckiematrixDB21JEnv
import time

env = DuckiematrixDB21JEnv(entity_name="map_0/vehicle_0")
obs, info = env.reset()

try:
    for step in range(500):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            obs, info = env.reset()
        time.sleep(0.1)  # 10 Hz control rate
finally:
    # Cleanup
    env.robot.camera.stop()
    env.robot.motors.stop()
    env.robot.reset_flag.stop()

