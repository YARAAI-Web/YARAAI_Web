rule auto_rule_20250726174910_6790 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "LocalSize" wide ascii nocase
    $o2 = "strpbrk" wide ascii nocase
    $o3 = "GetStringTypeW" wide ascii nocase
    $o4 = "dword_462DC8" wide ascii nocase
  condition:
    4 of ($o*)
}