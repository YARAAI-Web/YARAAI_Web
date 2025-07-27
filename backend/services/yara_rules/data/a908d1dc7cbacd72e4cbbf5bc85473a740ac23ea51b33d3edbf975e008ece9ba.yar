rule auto_rule_20250726192306_7548 {
  strings:
    $o0 = "dword_423484" wide ascii nocase
    $o1 = "_getenv_helper_nolock" wide ascii nocase
    $o2 = "_cropzeros" wide ascii nocase
    $o3 = "UnwindUp0_0" wide ascii nocase
  condition:
    4 of ($o*)
}