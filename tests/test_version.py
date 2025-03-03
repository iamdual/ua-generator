"""
Random User-Agent
Copyright: 2024-2025 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

from src.ua_generator.data.version import Version, WindowsVersion, AndroidVersion, ChromiumVersion


class TestVersion(unittest.TestCase):
    def test_version(self):
        version = Version(major=1, minor=2, build=3, patch=4)
        self.assertEqual(version.format(), '1.2.3.4')
        self.assertEqual(version.format(partitions=4), '1.2.3.4')
        self.assertEqual(version.format(partitions=3), '1.2.3')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 3, 4))

    def test_version_2(self):
        version = Version(major=1, minor=2, build=3, patch=None)
        self.assertEqual(version.format(), '1.2.3')
        self.assertEqual(version.format(partitions=4), '1.2.3.0')
        self.assertEqual(version.format(partitions=3), '1.2.3')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 3, 0))

    def test_version_3(self):
        version = Version(major=1, minor=2, build=None, patch=0)
        self.assertEqual(version.format(), '1.2.0.0')
        self.assertEqual(version.format(partitions=4), '1.2.0.0')
        self.assertEqual(version.format(partitions=3), '1.2.0')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 0, 0))

    def test_version_4(self):
        version = Version(major=1, minor=2, patch=4)
        self.assertEqual(version.format(), '1.2.0.4')
        self.assertEqual(version.format(partitions=4), '1.2.0.4')
        self.assertEqual(version.format(partitions=3), '1.2.0')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 0, 4))

    def test_version_5(self):
        version = Version(major=0, build=3)
        self.assertEqual(version.format(), '0.0.3')
        self.assertEqual(version.format(partitions=4), '0.0.3.0')
        self.assertEqual(version.format(partitions=3), '0.0.3')
        self.assertEqual(version.format(partitions=2), '0.0')
        self.assertEqual(version.format(partitions=1), '0')
        self.assertEqual(version.to_tuple(), (0, 0, 3, 0))

    def test_version_6(self):
        version = Version(major=1, minor=2)
        self.assertEqual(version.format(), '1.2')
        self.assertEqual(version.format(partitions=3), '1.2.0')
        self.assertEqual(version.to_tuple(), (1, 2, 0, 0))

    def test_version_7(self):
        version = Version(major=1)
        self.assertEqual(version.format(), '1')
        self.assertEqual(version.format(partitions=2), '1.0')
        self.assertEqual(version.to_tuple(), (1, 0, 0, 0))

    def test_version_none(self):
        version = Version(major=None, minor=None, build=None, patch=None)
        self.assertEqual(version.format(), '')
        self.assertEqual(version.format(partitions=1), '0')
        self.assertEqual(version.format(partitions=2), '0.0')
        self.assertEqual(version.to_tuple(), (0, 0, 0, 0))

    def test_version_separator(self):
        version = Version(major=1, minor=2, build=3, patch=4)
        self.assertEqual(version.format(separator='_'), '1_2_3_4')
        self.assertEqual(version.format(partitions=4, separator='_'), '1_2_3_4')
        self.assertEqual(version.format(partitions=3, separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=2, separator='_'), '1_2')
        self.assertEqual(version.format(partitions=1, separator='_'), '1')

    def test_version_separator_2(self):
        version = Version(major=1, minor=2, build=3, patch=None)
        self.assertEqual(version.format(separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=4, separator='_'), '1_2_3_0')
        self.assertEqual(version.format(partitions=3, separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=2, separator='_'), '1_2')
        self.assertEqual(version.format(partitions=1, separator='_'), '1')

    def test_version_separator_3(self):
        version = Version(major=1, minor=2, build=3, patch=0)
        self.assertEqual(version.format(separator='_'), '1_2_3_0')
        self.assertEqual(version.format(partitions=4, separator='_'), '1_2_3_0')
        self.assertEqual(version.format(partitions=3, separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=2, separator='_'), '1_2')
        self.assertEqual(version.format(partitions=1, separator='_'), '1')

    def test_version_trim_zero(self):
        version = Version(major=1, minor=2, build=0, patch=0)
        self.assertEqual(version.format(trim_zero=True), '1.2')

    def test_version_trim_zero_2(self):
        version = Version(major=1, minor=2, build=0, patch=4)
        self.assertEqual(version.format(trim_zero=True), '1.2.0.4')

    def test_version_trim_zero_3(self):
        version = Version(major=1, minor=None, build=3, patch=4)
        self.assertEqual(version.format(partitions=2, trim_zero=True), '1')

    def test_version_range(self):
        version = Version(build=(90, 100))
        self.assertTrue(version.build >= 90 and version.build <= 100)

    def test_version_windows(self):
        version = WindowsVersion(version=Version(major=10, minor=0), ch_platform=Version(major=1, minor=2))
        self.assertEqual(version.format(partitions=4), '10.0.0.0')
        self.assertEqual(version.ch_platform.format(partitions=4), '1.2.0.0')

    def test_version_windows_range(self):
        version = WindowsVersion(version=Version(major=10, minor=0), ch_platform=Version(major=(1, 10)))
        self.assertEqual(version.format(partitions=4), '10.0.0.0')
        self.assertTrue(version.ch_platform.major >= 1 and version.ch_platform.major <= 10)

    def test_version_android(self):
        version = AndroidVersion(version=Version(), build_numbers=('foo', 'bar'))
        self.assertIn(version.build_number, ('foo', 'bar'))

    def test_version_android_2(self):
        version = AndroidVersion(version=Version(), build_numbers=['foo', 'bar'])
        self.assertIn(version.build_number, ['foo', 'bar'])

    def test_version_android_3(self):
        version = AndroidVersion(version=Version(), build_numbers='foo')
        self.assertEqual(version.build_number, 'foo')

    def test_version_chromium(self):
        version = ChromiumVersion(Version(major=1, minor=2, build=3, patch=4), webkit=Version(537, 36))
        self.assertEqual(version.format(partitions=4), '1.2.3.4')
        self.assertEqual(version.webkit.format(), '537.36')

    def test_version_comparison(self):
        version_1 = Version(major=1, minor=2)
        version_2 = Version(major=1, minor=3)
        self.assertFalse(version_1 == version_2)
        self.assertTrue(version_1 != version_2)
        self.assertTrue(version_1 < version_2)
        self.assertFalse(version_1 > version_2)
        self.assertTrue(version_1 <= version_2)
        self.assertFalse(version_1 >= version_2)

    def test_version_comparison_2(self):
        version_1 = Version(major=1, minor=0)
        version_2 = Version(major=1, minor=0)
        self.assertTrue(version_1 == version_2)
        self.assertFalse(version_1 != version_2)
        self.assertFalse(version_1 < version_2)
        self.assertFalse(version_1 > version_2)
        self.assertTrue(version_1 <= version_2)
        self.assertTrue(version_1 >= version_2)


if __name__ == '__main__':
    unittest.main()
