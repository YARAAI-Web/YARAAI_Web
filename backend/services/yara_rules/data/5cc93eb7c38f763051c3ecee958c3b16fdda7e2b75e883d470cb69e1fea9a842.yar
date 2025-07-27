rule auto_rule_20250727011239_8770 {
  strings:
    $o0 = "GetLocaleInfoA" wide ascii nocase
    $o1 = "TrailDown0_0" wide ascii nocase
    $o2 = "report_failure" wide ascii nocase
    $o3 = "_seh_longjmp_unwind" wide ascii nocase
    $o4 = "dword_44C12C" wide ascii nocase
  condition:
    5 of ($o*)
}