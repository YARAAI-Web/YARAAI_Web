rule auto_rule_20250727011426_1055 {
  strings:
    $o0 = "dword_476AD0" wide ascii nocase
    $o1 = "_seh_longjmp_unwind" wide ascii nocase
  condition:
    all of them
}