rule auto_rule_20250726113749_1130 {
  strings:
    $o0 = "__crtExitProcess" wide ascii nocase
    $o1 = "dword_44C13C" wide ascii nocase
    $o2 = "dword_44C154" wide ascii nocase
  condition:
    3 of ($o*)
}