rule auto_rule_20250726074104_4262 {
  strings:
    $o0 = "TrailDown0_0" wide ascii nocase
    $o1 = "off_46B580" wide ascii nocase
    $o2 = "dword_46AEE4" wide ascii nocase
  condition:
    3 of ($o*)
}