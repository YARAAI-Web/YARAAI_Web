rule auto_rule_20250726151041_0959 {
  strings:
    $o0 = "dword_456D40" wide ascii nocase
    $o1 = "_global_unwind2" wide ascii nocase
    $o2 = "off_456494" wide ascii nocase
  condition:
    3 of ($o*)
}