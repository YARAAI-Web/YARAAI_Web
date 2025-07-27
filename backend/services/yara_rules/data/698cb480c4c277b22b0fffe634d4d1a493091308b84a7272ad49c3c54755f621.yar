rule auto_rule_20250726093220_7048 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "xmmword_415220" wide ascii nocase
    $o2 = "ReturnValue" wide ascii nocase
    $o3 = "x7FF8" wide ascii nocase
  condition:
    4 of ($o*)
}