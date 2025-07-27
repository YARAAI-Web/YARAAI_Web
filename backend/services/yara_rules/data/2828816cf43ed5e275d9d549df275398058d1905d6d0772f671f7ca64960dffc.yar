rule auto_rule_20250726095247_0693 {
  strings:
    $o0 = "dword_780E8" wide ascii nocase
    $o1 = "DriverEntry" wide ascii nocase
    $o2 = "dword_78168" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}