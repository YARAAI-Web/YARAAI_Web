rule auto_rule_20250726215216_5556 {
  strings:
    $o0 = "off_455ED0" wide ascii nocase
    $o1 = "dword_456358" wide ascii nocase
    $o2 = "dword_456098" wide ascii nocase
    $o3 = "__ascii_strnicmp" wide ascii nocase
  condition:
    4 of ($o*)
}