rule auto_rule_20250726231432_2871 {
  strings:
    $o0 = "dword_46801C" wide ascii nocase
    $o1 = "_cpinfo" wide ascii nocase
    $o2 = "fails" wide ascii nocase
    $o3 = "inconsistent" wide ascii nocase
  condition:
    4 of ($o*)
}