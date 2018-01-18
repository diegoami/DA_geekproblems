# code

"""
900  940 950  1100 1500 1800
910 1200 1120 1130 1900 2000
910 1120 1130 1200 1900 2000


1:
    9:00 --> +1
2:
    9:10 -->  0
3:
    9:40  -> 1
4:
    9:50  -> 2
5:
    11:00  -> 3
6:
    11:20  --> 2


"""
inputarray =[
"5",
"6",
"900  940 950  1100 1500 1800",
"910 1200 1120 1130 1900 2000",
"4",
"900 940 2400 400",
"940 950 200 420",
"4",
"1100 1200 1500 1800",
"1100 1200 1500 1800",
"5",
"1035 1040 1050 1500 1605",
"1040 1042 1055 1505 1610",
"2241",
"167 177 1932 2309 145 1240 627 1724 738 2339 1719 2083 1330 2142 34 2316 2240 859 1105 331 1978 2307 474 787 222 2346 525 2273 1471 1030 378 1174 298 2113 2387 1291 1962 1837 756 768 2056 1175 1632 53 951 1151 142 125 1967 1031 2308 1392 1208 1738 1058 288 1354 784 546 1710 1010 159 222 1789 1623 947 1107 1031 2014 369 901 1392 1963 1656 611 1560 1225 1338 2349 1684 1196 1642 1203 351 692 2037 2175 1421 2197 22 949 1600 469 485 1082 2335 54 2000 19 1539 2101 1389 1328 468 1329 494 649 884 1008 22 2311 1818 1214 2315 2310 417 2136 652 1401 450 2120 357 1199 1504 1425 1409 1045 1410 590 1503 796 1286 694 2344 1724 1588 515 2304 249 1201 1459 1819 1381 597 399 882 390 1599 1610 758 1273 2023 1739 293 1239 180 1391 858 759 1392 616 1289 2357 1912 1803 235 273 856 1129 1047 2363 87 2076 2034 1070 943 2245 1417 282 799 723 1852 422 900 1158 2077 1493 390 276 1113 201 111 1804 470 1062 289 1402 190 856 2024 203 986 183 686 689 227 2218 2158 233 2133 1770 2155 1722 390 777 130 2369 2293 2226 956 1035 2150 242 2313 1346 1261 119 1354 1740 424 1880 1997 2288 530 950 638 667 950 194 1596 898 1217 1887 1706 489 1883 456 1735 1315 2102 117 1472 987 264 1914 356 2386 854 913 1209 1833 1746 1914 1357 1922 359 2047 1583 482 1745 1597 1023 2330 2162 736 1251 1574 867 45 60 2293 40 454 825 2155 711 2346 1450 1187 1114 2075 1623 2169 2019 1988 306 1159 192 603 1226 78 2015 2115 1825 535 1875 373 960 2234 1671 288 1898 319 978 974 1071 1764 269 393 1986 703 1281 414 428 3 1700 1728 226 1544 1925 1424 1173 1062 2182 2204 1033 706 1194 1126 1032 1293 143 423 87 1065 701 2388 1161 814 2175 2271 371 236 2034 512 1761 2097 2268 86 551 141 1695 296 25 1620 2126 177 95 1059 2303 572 867 2279 994 2252 1485 1019 2065 1920 1553 401 1288 2261 1927 1811 2358 971 1116 2377 1428 44 1159 2365 310 683 287 766 1088 778 75 226 1628 830 729 1424 2121 2103 563 124 597 1338 1262 596 1326 1265 1061 1403 917 231 1127 212 1972 1612 1548 1954 2321 991 525 1389 164 141 1652 1863 1830 2101 914 2159 779 1166 1008 1878 1201 2059 1640 2304 761 158 2325 1678 309 1914 488 602 1251 61 829 994 985 206 1741 2312 2305 836 1157 1273 551 2024 86 1357 1617 1627 2158 1327 1358 538 1672 2270 562 897 1023 818 513 718 1897 1986 42 424 130 230 2166 1760 1733 697 1056 54 163 1185 935 1855 173 2258 2370 933 564 208 84 912 2036 468 1249 2276 939 2224 543 2155 1712 1142 976 2260 1026 822 1071 1627 735 806 584 2251 599 680 1102 194 735 1638 135 757 1994 577 1706 2163 949 1482 301 14 2242 656 856 1143 1863 1212 2078 1225 1479 1753 1644 1897 674 441 2114 876 873 819 611 1018 533 1713 1896 1170 2232 841 89 2286 2291 298 190 1991 746 154 115 1852 341 445 1659 336 1560 1593 406 1265 182 2104 1430 2176 1409 493 1198 750 757 1562 428 1668 742 2130 41 1414 375 1402 1278 1016 1484 1014 2393 1825 802 1793 1360 271 29 1628 1685 476 1987 1099 971 1488 2248 1405 504 2022 1064 907 2364 1811 572 1090 1441 165 1543 420 1714 392 1905 619 2033 751 1206 176 1540 304 1823 1899 1648 1585 1649 572 1065 1314 1476 2346 2313 747 1879 1770 863 1320 1986 1890 1545 466 1741 1646 1509 1919 1471 2 1924 1933 473 753 1088 2171 964 1102 304 24 1128 2001 570 2016 766 29 2344 1348 2089 544 638 810 64 250 2282 1589 1743 609 861 2022 1759 1155 1689 2147 691 750 844 2231 1621 749 668 2137 1584 1236 1027 786 2239 254 1630 1625 1349 724 960 1058 767 145 556 1719 1527 1412 1826 1156 2202 950 2297 1785 2316 1165 1743 876 1114 1743 2397 349 1073 1227 207 2174 430 1205 1906 1427 1013 176 1294 2166 1637 337 342 2015 1195 1057 1853 2337 2039 1283 1356 1816 1132 1431 1042 226 2012 1438 1787 491 1651 863 35 1294 754 2217 1453 2009 63 634 655 1904 2235 2304 2257 149 1525 318 1814 710 29 401 1881 2119 59 51 156 162 865 2304 1277 844 510 503 1162 2090 949 1283 1654 1875 2221 603 2124 1432 170 1479 1060 2209 1020 2372 1204 346 182 105 393 1486 1314 1899 790 723 1139 2238 1611 262 1435 509 362 1560 1694 1516 1270 938 70 59 301 1972 2265 718 1816 556 616 1531 640 1413 489 1683 1955 1686 1511 485 775 1181 1016 1952 1742 1316 1680 311 1899 1474 789 2378 1333 1157 2290 2114 409 942 1391 1724 2164 29 1185 779 1 272 1886 375 1072 1734 1268 2154 2296 969 1626 77 1230 2251 199 910 2294 2287 1281 517 250 268 1529 280 665 622 1206 1627 2017 317 1327 2267 288 1282 765 1341 887 1222 2063 322 1265 510 1216 1103 1074 325 2342 1546 563 2024 1132 7 269 2119 803 708 308 1882 1013 1937 231 115 410 1685 1957 291 2094 1197 353 1055 1346 309 249 292 1713 332 1315 2040 759 723 905 2196 1053 1270 280 1439 24 1519 1267 860 1299 2087 1997 263 234 159 23 1147 1593 1038 1526 1048 659 1803 2008 1699 1431 493 201 79 1600 1553 1249 1883 541 1916 2176 1563 2368 737 1598 219 698 1829 1852 417 231 2050 126 659 230 521 1341 761 748 1163 1656 1476 793 762 555 1999 1547 1515 547 1989 370 1439 1264 676 516 1922 476 1216 1329 1235 571 906 2265 358 163 2162 1725 550 670 331 724 1951 2334 1326 1311 538 1937 1538 1279 394 437 1915 1765 392 750 2336 106 1338 405 1938 224 2265 371 1609 1769 82 2286 1953 1574 2253 995 277 2227 1997 373 1450 241 375 2020 944 1412 1942 1090 1220 766 1406 386 1817 251 1616 210 1465 1967 94 1675 1510 1501 496 2374 1190 1162 2373 1169 959 2032 2269 227 2111 823 1975 1580 2111 1953 1783 1392 1096 965 875 1365 503 1856 2061 475 2173 422 2123 1548 2378 190 1606 1396 1195 751 1944 755 82 1013 2073 1840 1429 1113 163 1168 409 2016 1909 424 2160 35 405 687 1920 959 1146 407 967 1901 1768 893 188 2133 1757 2175 1048 222 1484 2223 532 2377 2184 549 724 1183 419 377 2021 2312 983 2257 291 1726 1925 1687 478 1570 2044 335 1278 1069 2269 392 997 584 29 528 627 1472 1098 813 1904 1428 1809 746 2309 2386 1439 238 44 2114 902 1651 1129 2112 2051 1750 1593 1455 1470 682 1066 1068 914 594 1835 1473 1773 1231 902 2043 378 1878 1771 703 2365 1382 2191 1624 2238 824 980 2196 970 2328 43 111 1783 1459 727 2288 1671 1329 852 2259 14 261 1784 2087 343 1411 2073 2329 1635 1042 1519 1104 468 866 1339 1882 2058 1151 2215 1799 2059 262 2064 1557 1608 1079 290 236 1566 876 387 1387 634 1161 1331 2049 1729 693 434 2241 1967 1736 611 2000 2238 293 783 129 553 1770 45 195 1809 2053 2048 633 2336 9 865 1098 1644 1250 416 442 190 1701 613 1849 2324 652 475 2234 1092 801 655 391 1698 120 981 979 932 1345 941 1488 900 926 1284 739 293 1394 1853 1012 1561 1435 1841 298 386 1730 341 2006 2392 1393 1211 1550 2379 580 2172 2078 74 994 1621 2298 1827 77 591 1783 1579 1560 1219 90 160 1050 925 1873 781 609 1568 609 1678 1704 971 1408 2197 75 1723 612 2220 2362 1457 891 2364 2284 1717 733 1453 342 155 2014 463 797 1061 1416 1305 200 937 2281 1999 633 2388 1385 41 1118 207 1471 242 2083 1250 1124 559 106 822 296 97 317 1279 579 1580 1059 1178 751 2008 2130 82 596 279 677 1354 1700 2185 1166 694 1609 1373 1644 1130 315 569 256 1592 1174 1723 1949 852 1387 2145 2047 378 118 230 1117 1075 1392 1070 1313 947 1894 1892 216 550 458 1441 2053 237 1352 2288 27 1763 156 1584 1195 1381 1698 666 666 114 2062 579 1879 79 2141 2212 748 46 171 1176 1490 751 1350 934 1866 615 483 608 1033 1697 1968 2123 83 611 842 32 2188 1906 1680 1522 1739 152 248 209 47 677 1760 1390 1623 1267 1287 1056 2029 815 61 454 2178 149 504 1262 832 283 456 2198 507 1553 1422 497 2282 2022 456 1548 725 1519 1936 1777 1775 1060 999 75 2054 2123 1036 1644 89 954 1233 2348 2281 727 1679 1651 402 962 2200 1656 2364 917 974 362 1646 1674 1875 1551 354 1182 1888 300 1311 1844 666 2373 130 382 2113 1477 1982 1048 491 2272 1606 1173 1233 1590 2121 1566 1032 59 1694 407 179 149 2207 772 1367 997 2298 2221 2095 1130 389 1310 1185 2370 179 18 1616 2227 1285 1969 1107 1929 98 1719 391 800 2186 87 2400 421 1511 1472 1414 1016 1286 319 1181 1332 68 1188 1445 1587 108 1961 1028 1675 32 2353 1472 669 2294 686 338 112 805 678 407 569 223 214 201 543 738 1239 2189 156 1290 448 782 1094 2185 1388 1162 1294 1018 2302 683 648 1266 1154 505 685 2296 1526 1422 1565 182 73 907 1257 944 994 681 1681 469 2212 1714 1769 852 817 80 2369 241 332 934 2180 1464 260 254 1537 2096 366 2275 521 436 1681 1777 1656 926 1672 809 1560 1957 803 1033 706 841 176 2363 1286 363 1881 1837 1198 3 909 481 541 77 1859 294 541 1347 1275 774 2298 1681 1736 1473 1801 708 1356 1467 1742 1989 482 369 1916 197 1826 1010 413 1337 1856 1963 1044 743 22 1123 513 2049 2019 969 2118 115 851 1291 936 760 770 296 504 1041 380 200 306 792 1862 1482 1253 1554 34 830 1588 2243 2254 884 1821 1415 1519 245 2264 30 1453 2065 2370 1671 606 1848 1595 2288 327 877 2124 1741 480 2391 1389 711 472 1146 422 2071 984 1990 2356 179 780 207 1263 936 1888 797 234 2089 936 580 1594 391 963 2166 1402 2306 2208 568 270 735 1472 1458 999 1146 1598 2219 1639 445 173 1364 1829 465 2 324 1491 405 402 228 1598 2093 572 1164 502 764 522 1166 622 1846 1811 496 2342 623 613 352 1416 856 994 1539 880 683 1609 655 1423 1508 246 1339 145 691 140 1555 605 2224 626 879 125 782 2331 934 1824 1395 331 2047 188 646 2006 1417 951 1290 939 364 1736 298 1010 31 1625 1909 338 475 721 973 694 1456 1935 2362 2257 1207 985 2276 1983 2120 1942 1633 685 780 280 1484 1468 2037 126 119 738 1229 920 1378 1138 2092 1357 1196 1661 302 1594 1033 2137 2181 476 1108 1985 1675 1520 391 1277 1242 952 1130 1891 1375 1473 1192 190 1388 291 840 494 654 264 1082 1904 606 177 1680 1696 1340 1269 1999 1884 2040 716 1222 1194 1427 1323 2239 829 582 400 1779 2292 1024 544 835 2244 150 303 1508 1303 1142 1088 1147 1492 638 1614 1801 1217 491 1163 1736 327 211 678 1783 2261 790 306 1875 264 1523 996 967 1961 1239 1789 612 1846 2268 1226 468 1190 943 1064 2348 1703 818 1900 1024 427 4 1249 1852 1571 1437 2259 1968 1257 2206 1932 1163 420 776 957 332 296 845 1792 404 989 2116 251 320 1473 1792 584 534 1776 643 1970 1501 1155 79 1186 2258 1334 894 891 504 2351 434 1123 272 412 2191 1539 42 1659 2248 2353 59 480 1303 1484 2191 403 1169 2023 96 1336 1209 362 2343 595 2100 1589 979 1643 158 2342 1848 270 1946 1981 714 565 1711 862 1386 874 1105 2263 1504 1703 1470 355 1130 353 875 2350 1331 2245 1245 1050 2119 66 2364 353 2374 1671 932 1948 312 1070 2399 899 2304 953 1680 1654 1044 123 2289 1564 1835 251 223 41 312 2293 852 2181 1078 1217 1077 2379 421 216 749 399 980 436 58 484 1663 2103 1863 221 571 2223 2074 1842 687 89 1518 518 1893 1699 1668 2150 66 790 2133 1620 1682 2004 331 1029 1832 190 1553 1831",

"2373 665 1608 296 1429 882 1691 211 2178 2272 1237 1660 1444 41 1234 638 2294 1031 1075 994 2383 1004 662 1091 463 708 1798 2352 1624 1691 2318 1841 2304 767 84 2062 1060 1446 1187 1452 1566 402 41 410 1498 884 451 1259 1222 176 1782 388 872 1888 1600 505 980 2139 1101 531 62 119 206 341 2029 460 2023 2399 1361 699 936 882 1815 368 1694 2197 2362 547 939 471 1339 2277 2356 918 1972 2361 953 1759 1034 1056 266 727 2 635 760 794 1749 874 1993 1794 934 1338 304 1291 1812 1695 669 1428 299 990 849 1480 2048 1550 2132 670 2076 1599 1450 1437 600 924 1444 1732 1355 1262 2035 2186 2368 1217 1794 2305 1067 2154 1509 1824 1885 1993 1068 449 1270 1931 2012 615 1691 628 2144 1605 1000 2075 2396 507 359 790 259 1410 1090 1848 41 1419 2165 1176 27 1090 104 1267 13 2041 571 277 1396 2242 1187 852 1910 988 884 1886 1791 51 1887 2356 1782 1729 1503 278 2063 25 1166 1473 833 2086 29 1847 1690 1679 1284 926 2066 61 246 1579 1022 1856 121 928 774 1135 852 1076 1337 1935 1802 338 2111 1175 391 1157 1072 881 1336 946 483 1826 1919 1574 2313 1038 199 306 2363 1718 1493 340 1648 1347 2304 1432 116 840 1859 1630 246 995 400 446 2273 676 263 873 1774 81 1639 498 1143 809 4 1678 1326 935 1402 1879 1583 970 1537 1079 1140 1939 1922 227 1064 1678 2376 1925 1982 1301 762 63 1603 1649 1096 685 17 738 2308 1994 2085 545 1460 822 2259 644 869 1078 120 1058 1442 1692 1265 1624 2116 873 1130 842 2316 816 537 558 1360 701 1453 294 242 2230 449 428 2199 1825 725 275 1334 1286 639 171 2063 1430 285 2310 479 2124 686 601 1425 2194 1506 2213 1366 968 1008 1078 1785 705 391 235 1292 622 1286 1335 1191 1343 1199 487 819 1222 1625 998 2177 255 870 1309 928 494 2069 1567 1903 39 601 1220 2319 2291 585 1940 157 1809 2233 2279 415 1788 40 1675 1021 1228 155 1989 242 2399 1643 2203 1922 1305 1947 2257 1710 1034 909 562 1734 1487 405 2386 543 2043 461 562 421 1944 2379 1188 114 1064 2192 1135 1216 657 962 1013 2012 2360 1852 1939 1371 2125 708 808 785 1352 1502 90 959 1042 1791 214 1613 456 1861 2294 1273 1403 1477 1544 174 1467 1252 876 2329 533 1162 670 1304 1530 308 1493 52 1154 1993 971 1520 273 1808 895 2306 2041 1184 2263 2210 2208 1239 1961 672 1572 1455 1148 1915 124 2030 490 1967 1088 957 233 271 1740 1467 1323 84 961 754 706 692 1260 1387 488 2230 43 1918 446 357 1389 1453 755 1667 2234 1361 520 1632 1939 2068 1777 1899 315 1921 1054 8 2070 217 123 643 208 1064 2261 2148 1794 2231 1918 1444 177 1315 2227 318 1335 1421 2172 393 1765 2355 2067 294 1865 2176 1001 213 1901 352 1477 1580 1344 1078 1390 362 1786 1073 1835 745 762 1564 105 947 2289 1109 158 1431 324 1665 1675 1947 1838 1982 1319 212 1893 792 1433 724 1662 192 262 931 2099 570 492 1201 2180 118 2318 715 1596 1442 1137 268 2229 254 1510 1974 1182 1904 170 2017 1884 1368 586 2003 431 358 2282 1168 1111 1867 1288 1172 1078 46 1565 1439 1272 2048 2116 2193 912 1458 1406 54 2372 1381 1141 931 1676 321 1791 1378 1399 2187 5 2090 432 945 1189 211 1919 520 1460 1128 210 1720 2280 1117 1501 2197 54 1859 1631 594 2007 1050 455 273 2161 295 55 2334 147 1830 872 829 960 642 622 1089 1967 34 286 2271 1330 1062 1261 2209 1783 563 1307 2079 2380 1898 688 1739 70 1984 741 1196 67 1834 1510 558 2318 2135 854 1336 259 194 1044 94 2067 1352 1341 1495 938 375 113 1298 2352 296 218 1893 2093 1038 1131 614 1297 111 1190 829 1010 2387 545 2041 983 2170 1321 994 1493 563 2215 528 408 1195 1506 314 2212 2114 1894 465 2204 196 963 2382 547 1110 1049 169 225 912 755 1836 1128 234 1841 1863 728 1178 2218 2341 543 701 2001 1759 2277 755 1336 2031 1032 2096 1138 1224 1123 528 1630 1412 1812 2155 481 254 894 2122 1586 129 844 2201 956 672 2071 253 2176 232 1641 1735 1241 787 35 2249 1540 2366 797 713 63 1053 1932 2388 465 1358 2249 757 971 651 783 102 1294 100 1733 2245 1132 76 2205 2251 627 2067 2139 602 424 1844 442 981 496 719 1260 1364 629 1530 1089 55 1414 980 1770 667 480 1178 1438 1003 1516 1693 1724 473 649 1524 1554 1549 396 1198 2109 1309 612 1994 466 382 803 811 829 857 1306 1766 1224 1570 2116 1054 606 2085 679 946 241 834 86 501 1369 2395 2234 1886 349 1482 1233 1857 1111 1273 1783 2302 307 1036 1061 1272 728 2338 1144 169 1834 1596 372 404 143 1212 680 2235 113 594 531 2162 1635 659 327 1107 392 44 1389 1428 1520 85 425 2294 1636 1225 1695 1183 1668 1428 406 1547 1487 2190 1341 1438 1251 1960 2379 157 1478 4 1643 1501 1412 426 1944 2396 1817 216 5 1807 1969 442 1536 699 1326 1914 1624 713 619 1658 1597 1140 1887 895 647 644 323 912 1881 1856 2359 448 71 991 1474 1928 1014 1055 697 473 451 442 2242 847 1926 1814 25 1130 1496 1404 595 794 2068 588 2241 1080 442 1326 535 61 1401 108 1422 1293 1294 318 518 1204 1544 1094 1040 212 526 29 779 1149 451 1293 45 1055 2024 354 37 348 2147 827 1662 1505 639 772 487 2006 500 457 2129 1268 1352 2020 792 1367 918 1847 294 788 1422 1313 2068 1900 1245 1098 1202 929 943 2305 1769 969 242 1897 1663 1121 2045 1519 26 2020 785 1375 1385 860 1150 215 896 504 233 1852 1538 415 1164 2252 1220 291 1918 84 719 185 853 1187 70 2249 138 2398 425 1569 828 1749 794 783 472 1270 894 1678 1015 2305 485 544 1896 412 1294 93 1999 1991 1700 491 1294 275 1550 1775 2115 974 70 419 466 34 839 712 1253 1664 1709 1150 1489 246 1432 721 507 72 369 1622 859 1758 48 183 1439 123 924 907 1907 590 1557 1546 352 2124 2319 351 2098 2237 992 1407 2111 1814 252 1881 1445 744 542 1646 179 150 106 515 586 2028 1425 405 1957 2318 1428 556 503 2287 269 2099 1780 2212 490 1159 1491 1976 2011 333 690 897 2351 1513 923 530 473 1837 1478 754 1977 1071 1886 1453 1752 1598 552 202 436 2294 673 1117 1917 1329 1512 926 2239 897 2140 1945 1057 827 903 359 589 22 987 2109 978 629 380 548 550 1281 1246 1129 2063 827 2320 1078 292 1648 1786 1632 207 1485 355 2370 310 1557 822 1546 1466 1617 261 2098 1536 391 878 1650 1806 687 1789 1876 1144 578 531 2088 156 883 1254 601 1355 290 1289 1216 9 111 941 1400 598 108 1255 305 1038 886 500 1993 814 1413 1883 984 952 1730 338 234 2201 665 2084 2258 1769 1711 369 509 242 1333 438 2085 1300 1502 1070 2184 457 493 441 88 613 1811 1021 436 1664 1016 1898 1878 375 535 1154 334 79 2287 1625 335 1276 950 1913 585 1825 1393 1705 23 1656 2114 463 474 885 161 2323 2054 198 2223 551 2138 1918 1607 132 598 1106 437 758 1800 1891 1899 986 2248 1085 593 1926 1797 1056 829 939 543 29 996 1943 1238 707 1968 254 194 2106 147 1210 1925 655 666 240 2207 210 1093 2100 1376 2237 1462 1648 1219 1014 328 1313 1497 310 1442 931 1891 1835 716 1487 1124 1467 1345 1537 438 617 1094 1950 2172 1245 1178 86 2201 191 686 1926 319 1669 407 130 9 142 226 1137 2381 717 1671 985 2348 1129 1537 1405 1101 324 2365 1412 1641 251 1905 1884 167 1742 271 1246 907 1889 1657 1108 1067 1058 1079 2200 675 2156 1192 1791 1033 2059 1397 1718 1891 1568 1708 1035 1847 1863 203 1040 1027 2296 2107 1115 751 2187 480 977 1823 2080 1102 1413 877 765 158 1371 1239 313 545 2162 1781 1401 1844 257 1262 248 1140 609 2091 653 980 1419 2220 8 685 548 1178 1276 1814 1910 1372 2243 1940 1537 1422 2302 2035 1330 2159 1437 2070 1298 2105 2399 1803 1506 1239 633 866 517 82 1180 1824 1728 1772 114 783 1341 817 2089 920 790 714 1460 1652 1072 1684 1965 639 613 785 160 1902 2375 2334 260 1315 1250 1796 2123 542 1217 978 1053 566 692 139 1311 1768 656 1788 825 1423 2040 1042 1849 405 1435 169 242 1673 1469 775 2377 338 1434 842 946 1219 2216 1375 53 847 1757 1525 2167 1182 945 1041 535 897 2277 1028 1206 2019 1892 442 1466 1792 872 1460 2101 1018 2017 1944 225 265 306 1158 303 467 2076 847 833 990 1247 2146 1204 1153 702 1127 354 1985 450 1551 806 347 1026 171 2337 2396 194 1724 733 57 1497 811 977 893 151 891 1796 1853 551 1116 437 562 1361 385 1530 135 1251 1683 7 1937 1585 1191 18 383 2267 1517 1589 2226 1102 811 1651 783 2222 394 639 2355 2194 496 1081 839 1168 621 1946 84 2266 697 2034 791 1033 990 1040 984 1818 530 1954 1080 1814 1001 1053 746 662 2152 1919 164 614 508 755 277 618 1612 1430 2265 1567 332 1143 1099 323 2356 1188 858 1559 2065 1763 1311 2147 2266 1181 1166 1147 1541 898 843 65 1595 585 671 1516 1001 1207 907 103 697 1634 412 2268 416 1846 1376 1555 1849 920 1080 1589 2322 393 398 598 1510 1453 72 659 2123 460 798 1400 1900 1721 1321 837 185 113 1916 2354 286 1542 600 1968 1809 2045 1370 882 80 1909 408 460 1707 2250 76 1627 925 1208 975 485 929 547 746 1282 2115 950 169 1339 1108 394 1905 1106 1698 1418 1556 2242 2344 2134 898 680 1537 356 1634 1955 931 653 705 1080 489 871 555 2073 977 302 1016 1287 1832 681 776 1461 1315 1739 2258 591 239 182 1048 443 619 1671 1632 62 820 2382 1791 834 1473 1564 2103 503 529 1922 899 248 1346 2007 2223 1487 995 1978 845 1884 2348 1241 486 2065 524 1138 2254 769 1731 856 1467 59 913 857 919 1202 143 2077 307 1503 1085 624 1471 2313 1051 1476 1112 451 2396 689 1921 2102 984 799 1493 2049 1985 1446 188 63 1944 1459 60 1672 2017 973 1233 442 884 1689 416 1977 1717 1499 40 84 806 798 347 970 2076 918 2188 621 1231 643 136 1190 1174 1081 74 1178 787 1182 586 523 1546 1780 1686 1314 2136 536 2084 2187 1697 1449 2086 353 522 2061 383 1837 489 720 437 393 666 79 1799 297 2387 1812 1377 348 122 1603 46 1903 2165 340 173 2258 2371 321 455 160 1481 99 1792 2361 1711 792 1868 434 1676 137 1700 976 1791 2377 57 1073 1504 287 1768 2316 1943 1896 1167 1657 2187 1238 2399 627 1565 1086 466 2109 1141 1361 415 1955 1213 553 939 1507 526 1831 450 1580 680 1114 39 1318 1222 2146 1192 1970 240 309 2166 2163 274 2082 371 1548 654 1109 1709 2316 2030 2267 1290 264 2172 742 1860 1832 1973 115 1367 1989 1371 1769 600 656 1451 1445 937 1879 207 628 714 324 1172 1728 274 1862 2174 335 2303 1588 218 264 1354 2127 1396 1496 414 7 971 2260 1706 897 834 224 53 1080 1720 1327 594 386 2266 172 1045 308 472 88 1700 2120 1397 916 753 893 354 1058 1191 960 1358 1287 610 1066 1687 820 260 714 36 1029 1702 869 1270 457 1932 379 2075 1796 2044 75 1317 625 1712 1786 923 1772 458 2096 975 239 2184 259 496 1723 184 1432 704 2233 301 1191 2281 609 1106 1503 1259 219 958 1162 121 229 2057 1714 933 1493 383 68 1721 159 1875 1588 1895 184 2165 865 515 347 391 826 2256 1164 268 993 2232 1020 481 2319 1729 749 2321 1880 892 1367 1188 1009 127 426 2360 719 821 436 115 1457 148 357 1335 961 752 1809 279 695 590 725 777 95 1691 990 573 220 1502 103 845 1324 140 1410 2228 1838 987 1017 1828"



]
from tools import input, initArrayInputter
initArrayInputter(inputarray)

def prepr(ld, la):
    hc, mc = 0, 0
    dd = 0
    od, oa = [], []
    for i,l in enumerate(ld):
        hd, md = l // 100, l % 100
        ha, ma = la[i] // 100, la[i] % 100
        if hd < hc:
            dd = dd + 1
        td, ta = (dd*24+hd)*60+md, (dd * 24 + ha) * 60 + ma
        while td > ta:
            ta = ta + 24*60
        od.append(td)
        oa.append(ta)

        hc, mc = hd, md

    return od, oa


def find_platforms(n, ld, la):
    #    s = {la[i] : ld[i] for i in range(la)}
    ld, la = prepr(ld, la)

 #   print(ld)
 #   print(la)
    la = sorted(la)
    id, ia = 0, 0
    mpn, pn = 0, 0
    lcnt = 0
    cid, cia =  ld[0], la[0]
    while (id < n or ia < n) and lcnt < 30:
        lcnt += 1

#        print(cid, cia)
        if cid < cia and id < n:
            pn += 1
            id = id + 1
            if id < n:
                cid = ld[id]
        else:
            pn -= 1
            ia = ia + 1
            if ia < n:
                cia = la[ia]

        if pn > mpn:
            mpn = pn

    return max(mpn,1)




from sys import stdin

t = int(input())
for _ in range(t):
    n = int(input())
    ld = list(map(int, input().split()))
    la = list(map(int, input().split()))
    pn = find_platforms(n, ld, la)
    print(pn)