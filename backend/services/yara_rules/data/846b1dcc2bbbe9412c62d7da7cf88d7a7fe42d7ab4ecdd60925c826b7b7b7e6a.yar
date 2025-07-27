rule auto_rule_20250727010008_7965 {
  strings:
    $o0 = "overrun" wide ascii nocase
    $o1 = "dword_466014" wide ascii nocase
    $o2 = "__ascii_stricmp" wide ascii nocase
  condition:
    3 of ($o*)
}