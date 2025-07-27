rule auto_rule_20250726125425_5131 {
  strings:
    $o0 = "dword_46ED50" wide ascii nocase
    $o1 = "dword_46E968" wide ascii nocase
    $o2 = "x41C4u" wide ascii nocase
    $o3 = "off_46E754" wide ascii nocase
  condition:
    4 of ($o*)
}