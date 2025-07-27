rule auto_rule_20250726084329_6246 {
  strings:
    $o0 = "dword_4643E0" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
    $o2 = "int64_arg" wide ascii nocase
    $o3 = "_tmpfname" wide ascii nocase
  condition:
    4 of ($o*)
}