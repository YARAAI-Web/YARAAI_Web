rule auto_rule_20250727041001_1605 {
  strings:
    $o0 = "dword_411960" wide ascii nocase
    $o1 = "dword_411980" wide ascii nocase
    $o2 = "_nh_malloc" wide ascii nocase
  condition:
    3 of ($o*)
}