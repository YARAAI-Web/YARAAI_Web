rule auto_rule_20250726194541_4034 {
  strings:
    $o0 = "dword_465468" wide ascii nocase
    $o1 = "fdwDetails" wide ascii nocase
    $o2 = "_fptrap" wide ascii nocase
    $o3 = "memcpy_0" wide ascii nocase
  condition:
    4 of ($o*)
}