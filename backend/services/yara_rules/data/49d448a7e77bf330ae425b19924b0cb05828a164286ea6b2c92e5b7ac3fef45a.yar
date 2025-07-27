rule auto_rule_20250726170837_7493 {
  strings:
    $o0 = "dword_41813C" wide ascii nocase
    $o1 = "asc_413028" wide ascii nocase
    $o2 = "PeekNamedPipe" wide ascii nocase
  condition:
    3 of ($o*)
}