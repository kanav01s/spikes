import csv
import os

from hdfaccess.file import hdf_file

from analysis_engine.library import most_common_value

from data_exports.formats import csv_file
from polaris_tasks.analysis_utils import get_flight_info
from polaris_tasks.utils import copy_to_outbound
from polaris_tasks.status_tasks import queue_task

from polariswebsite.DB.models import Flight


FLIGHT_TAPE_CFG = {
    'name': 'Edge Aerodynamics',
    'filename_format':  '{Fleet}_{Tail Number}_{Takeoff Airport IATA}_{Landing Airport IATA}_{Flight Hash:.12}_{Flight ID}_edge_aerodynamics',
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

CSV_FN_FORMAT = 'ALL id={Flight Hash:.12} ac={Tail Number} ' \
    'dt={Takeoff Datetime.year}{Takeoff Datetime.month:02d}{Takeoff Datetime.day:02d}'


SFTP_HOST = 'sftp.flightdataservices.com'
SFTP_USERNAME = 'cds_transfer'
SFTP_PASSWORD = 'Use6Act!'
# SFTP_PATH = '/data/Rolls Royce/Flight Tapes/CPA-A330-201611'
SFTP_PATH = '/data/Rolls Royce/Flight Tapes/CPA-A330-201702'


def flight_tape(flight):
    cfg = FLIGHT_TAPE_CFG.copy()
    phase = flight.phases.filter(name='CDS Flight Sector').first()
    if phase:
        cfg['start_index'] = phase.slice_start
        cfg['stop_index'] = phase.slice_stop
    flight_info = get_flight_info(flight)
    csv_fn = csv_file.get_filename(CSV_FN_FORMAT, flight_info)

    if not os.path.exists(csv_fn):
        csv_file.write_csv(
            flight.segment.file, csv_fn, cfg, flight_info=flight_info)

    return csv_fn


def get_esns(flight):
    try:
        with hdf_file(flight.segment.file, read_only=True) as hdf:
            e1esn = most_common_value(hdf['Eng (1) ESN'].array)
            e2esn = most_common_value(hdf['Eng (2) ESN'].array)
        return e1esn, e2esn
    except:
        import traceback
        traceback.print_exc()
        return '', ''


def send_file(fn):
    src_path = copy_to_outbound(fn, 'SFTP', 'cds_transfer@' + SFTP_HOST)
    dst_path = os.path.join(SFTP_PATH, fn)
    queue_task(
        'transfer.FileTransferSFTPTask',
        args=(src_path, dst_path, SFTP_USERNAME, SFTP_PASSWORD, SFTP_HOST),
    )


def flight_tapes(flights, summary_fn):
    n = 0
    with open(summary_fn, 'w+') as f:
        c = csv.writer(f)
        c.writerow(
            ('Filename', 'Flight hash', 'MSN', 'Eng (1) ESN', 'Eng (2) ESN'))
        for flight in flights:
            e1esn, e2esn = get_esns(flight)
            fn = flight_tape(flight)
            send_file(fn)
            c.writerow(
                (fn, flight.hash, flight.aircraft.manufacturer_number, e1esn, e2esn))
            n += 1
            if n % 1000 == 0:
                print n

    send_file(summary_fn)


def edge_aero_flight_tapes():
    """
    from 1 january 2016 to 3/7/17  flight tapes for specified tails.
    """
    TAILS = [
        'ZS-JRL', 'ZS-JRK', 'ZS-SJR', 
    ]

    flights = Flight.objects.filter(
        takeoff_datetime__gte='2016-01-01',
        takeoff_datetime__lt='2017-03-07',
        aircraft__tail_number__in=TAILS)

    print 'Processing %d flights' % flights.count()
    summary_fn = 'edge_aero_flight-tapes_summary.csv'
flight_tapes(flights, summary_fn)