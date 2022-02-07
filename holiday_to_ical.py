#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: se ai si et ts=3 sw=4 fenc=utf-8


import datetime
import sys
import uuid


def main(fin, fout):
    ical_lines = [
            'BEGIN:VCALENDAR',
            'VERSION:2.0',
            'PRODID:northtea',
            'CALSCALE:GREGORIAN',
            'X-WR-CALNAME:中国法定节假日',
            'X-WR-TIMEZONE:Asia/Shanghai',
            'X-APPLE-LANGUAGE:zh',
            'X-APPLE-REGION:CN',
            ]

    now = datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ');

    for line in fin.xreadlines():
        tokens = line.strip().split(':')
        if len(tokens) != 2:
            continue
        day = tokens[0]
        desc = tokens[1]

        ical_lines.extend([
            'BEGIN:VEVENT',
            'UID:' + str(uuid.uuid4()),
            'DTSTAMP:' + now,
            'DTSTART;VALUE=DATE:' + day,
            'CLASS:PUBLIC',
            'SUMMARY;LANGUAGE=zh_CN:' + desc,
            'TRANSP:TRANSPARENT',
            'CATEGORIES:HOLIDAY',
            'END:VEVENT',
            ]);

    ical_lines.append('END:VCALENDAR')

    for line in ical_lines:
        fout.write(line)
        fout.write('\r\n')


if __name__ == '__main__':
    main(sys.stdin, sys.stdout)


