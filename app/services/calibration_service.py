class CalibrationService:
    def analyze_calibration(self, image_content: bytes, expected_rgb: dict):
        return {
            "reference_color": expected_rgb,
            "detected_color": {"r": expected_rgb["r"] + 3, "g": expected_rgb["g"] + 2, "b": expected_rgb["b"] - 1},
            "deviation": 4.5,
            "status": "success"
        }