rule auto_rule_20250726141535_2831 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "dword_46151C" wide ascii nocase
    $o2 = "UnwindUp3_0" wide ascii nocase
    $o3 = "byte_444BB0" wide ascii nocase
  condition:
    4 of ($o*)
}