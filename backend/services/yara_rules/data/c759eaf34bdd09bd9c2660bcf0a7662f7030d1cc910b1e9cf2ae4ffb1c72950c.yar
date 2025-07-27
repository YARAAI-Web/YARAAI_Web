rule auto_rule_20250726151016_4923 {
  strings:
    $o0 = "dword_443F3C" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "dword_4431E0" wide ascii nocase
  condition:
    3 of ($o*)
}