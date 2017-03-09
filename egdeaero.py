CONFIGURATION = {
    'name': 'Edge Aerodynamics',
    'filename_format': '{Fleet}_{Tail Number}_{Takeoff Airport IATA}_{Landing Airport IATA}_{Flight Hash:.12}_{Flight ID}_edge_aerodynamics',
    'path_format': '{Tail Number}',
    'columns': [
        ('Index', '%.4f', ('Index',), None, True),
        ('Datetime', '%Y-%m-%d %H:%M:%S', ('Date',), None, True),
        ('Aircraft Energy', '%.4f', ('Aircraft Energy',), None, True),
        ('Airspeed True', '%.4f', ('Airspeed True',), None, True),
        ('Altitude STD', '%.0f', ('Altitude STD',), None, True),
        ('AOA', '%.1f', ('AOA',), None, True),
        ('AT N1', '%.1f', ('AT N1',), None, True),
        ('ECS Pack (1)', '%.1f', ('ECS Pack (1)',), None, True),
        ('ECS Pack (1) High Flow', '%.1f', ('ECS Pack (1) High Flow',), None, True),
        ('ECS Pack (1) On', '%.1f', ('ECS Pack (1) On',), None, True),
        ('ECS Pack (2)', '%.1f', ('ECS Pack (2)',), None, True),
        ('ECS Pack (2) High Flow', '%.1f', ('ECS Pack (2) High Flow',), None, True),
        ('ECS Pack (2) On', '%.1f', ('ECS Pack (2) On',), None, True),
        ('Elevator', '%.4f', ('Elevator',), None, True),
        ('Eng (1) Anti Ice', '%.4f', ('Eng (1) Anti Ice',), None, True),
        ('Eng (1) Bleed', '%.4f', ('Eng (1) Bleed',), None, True),
        ('Eng (1) Fuel Burn', '%.4f', ('Eng (1) Fuel Burn',), None, True),
        ('Eng (1) Fuel Flow', '%.4f', ('Eng (1) Fuel Flow',), None, True),
        ('Eng (1) N1', '%.4f', ('Eng (1) N1',), None, True),
        ('Eng (1) N1 Target', '%.4f', ('Eng (1) N1 Target',), None, True),
        ('Eng (1) N1 Trim', '%.4f', ('Eng (1) N1 Trim',), None, True),
        ('Eng (1) N2', '%.4f', ('Eng (1) N2',), None, True),
        ('Eng (1) Throttle Lever', '%.4f', ('Eng (1) Throttle Lever',), None, True),
        ('Eng (1) Throttle Rate Command', '%.4f', ('Eng (1) Throttle Rate Command',), None, True),
        ('Eng (2) Anti Ice', '%.4f', ('Eng (2) Anti Ice',), None, True),
        ('Eng (2) Bleed', '%.4f', ('Eng (2) Bleed',), None, True),
        ('Eng (2) Fuel Burn', '%.4f', ('Eng (2) Fuel Burn',), None, True),
        ('Eng (2) Fuel Flow', '%.4f', ('Eng (2) Fuel Flow',), None, True),
        ('Eng (2) N1', '%.4f', ('Eng (2) N1',), None, True),
        ('Eng (2) N1 Target', '%.4f', ('Eng (2) N1 Target',), None, True),
        ('Eng (2) N1 Trim', '%.4f', ('Eng (2) N1 Trim',), None, True),
        ('Eng (2) N2', '%.4f', ('Eng (2) N2',), None, True),
        ('Eng (2) Throttle Lever', '%.4f', ('Eng (2) Throttle Lever',), None, True),
        ('Eng (2) Throttle Rate Command', '%.4f', ('Eng (2) Throttle Rate Command',), None, True),
        ('Eng Bleed Open', '%.4f', ('Eng Bleed Open',), None, True),
        ('Flap', '%.4f', ('Flap',), None, True),
        ('Fuel Qty', '%.4f', ('Fuel Qty',), None, True),
        ('Fuel Qty (1) Imbalance Tank', '%.4f', ('Fuel Qty (1) Imbalance Tank',), None, True),
        ('Fuel Qty (2) Imbalance Tank', '%.4f', ('Fuel Qty (2) Imbalance Tank',), None, True),
        ('Fuel Qty (C)', '%.4f', ('Fuel Qty (C)',), None, True),
        ('Fuel Qty (L)', '%.4f', ('Fuel Qty (L)',), None, True),
        ('Fuel Qty (R)', '%.4f', ('Fuel Qty (R)',), None, True),
        ('Gross Weight Smoothed', '%.4f', ('Gross Weight Smoothed',), None, True),
        ('Heading Rate', '%.4f', ('Heading Rate',), None, True),
        ('Heading True Continuous', '%.4f', ('Heading True Continuous',), None, True),
        ('Impact Pressure', '%.4f', ('Impact Pressure',), None, True),
        ('Isolation Valve Open', '%.4f', ('Isolation Valve Open',), None, True),
        ('Kinetic Energy', '%.4f', ('Kinetic Energy',), None, True),
        ('Mach', '%.4f', ('Mach',), None, True),
        ('Pitch', '%.4f', ('Pitch',), None, True),
        ('Pitch Rate', '%.4f', ('Pitch Rate',), None, True),
        ('Potential Energy', '%.4f', ('Potential Energy',), None, True),
        ('Rudder', '%.4f', ('Rudder',), None, True),
        ('SAT', '%.4f', ('SAT',), None, True),
        ('SAT International Standard Atmosphere', '%.4f', ('SAT International Standard Atmosphere',), None, True),
        ('Stabilizer', '%.4f', ('Stabilizer',), None, True),
        ('Static Press', '%.4f', ('Static Press',), None, True),
        ('TAT', '%.4f', ('TAT',), None, True),
        ('Turbulence', '%.4f', ('Turbulence',), None, True),
        ('Vertical Speed', '%.4f', ('Vertical Speed',), None, True),
        ('Wind Direction True Continuous', '%.4f', ('Wind Direction True Continuous',), None, True),
        ('Wind Speed', '%.4f', ('Wind Speed',), None, True),
        ('Wing Anti Ice', '%.4f', ('Wing Anti Ice',), None, True),
        ('Zero Fuel Weight', '%.4f', ('Zero Fuel Weight',), None, True),    

    ],
    'bzip2': False,
    'frequency': 1,
    'step': 60,
    'header_row': True,
    'units_header_row': False,    
}
