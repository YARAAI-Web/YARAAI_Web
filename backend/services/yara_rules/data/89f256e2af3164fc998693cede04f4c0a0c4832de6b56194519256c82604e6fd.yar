rule auto_rule_20250726192256_8515 {
  strings:
    $o0 = "dwCreationDisposition" wide ascii nocase
    $o1 = "OemToCharW" wide ascii nocase
    $o2 = "uLockCode" wide ascii nocase
    $o3 = "lpConsoleCurrentFont" wide ascii nocase
  condition:
    4 of ($o*)
}