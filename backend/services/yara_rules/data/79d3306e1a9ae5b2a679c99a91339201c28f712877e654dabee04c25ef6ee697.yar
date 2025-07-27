rule auto_rule_20250726063523_1113 {
  strings:
    $o0 = "TrailDown0_0" wide ascii nocase
    $o1 = "aInconsistentIo" wide ascii nocase
    $o2 = "dword_46399C" wide ascii nocase
    $o3 = "off_463C40" wide ascii nocase
    $o4 = "UnwindUp2_0" wide ascii nocase
  condition:
    4 of ($o*)
}