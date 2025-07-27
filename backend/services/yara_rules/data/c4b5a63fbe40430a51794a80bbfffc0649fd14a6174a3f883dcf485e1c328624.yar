rule auto_rule_20250726084828_8697 {
  strings:
    $o0 = "dword_45577C" wide ascii nocase
    $o1 = "_NLG_Notify1" wide ascii nocase
    $o2 = "UnwindUp3_0" wide ascii nocase
  condition:
    3 of ($o*)
}