rule auto_rule_20250726102620_4678 {
  strings:
    $o0 = "dword_475E28" wide ascii nocase
    $o1 = "x4136A5" wide ascii nocase
    $o2 = "finish_loop" wide ascii nocase
    $o3 = "_NLG_Notify1" wide ascii nocase
  condition:
    4 of ($o*)
}