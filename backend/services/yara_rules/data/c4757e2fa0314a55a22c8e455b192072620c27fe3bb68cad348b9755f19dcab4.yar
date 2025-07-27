rule auto_rule_20250727013745_6564 {
  strings:
    $o0 = "strncnt" wide ascii nocase
    $o1 = "dword_46444C" wide ascii nocase
    $o2 = "_CrtCheckMemory" wide ascii nocase
  condition:
    3 of ($o*)
}