rule auto_rule_20250726195045_9085 {
  strings:
    $o0 = "szWindow" wide ascii nocase
    $o1 = "x4923u" wide ascii nocase
    $o2 = "dword_43385F" wide ascii nocase
    $o3 = "x3975" wide ascii nocase
    $o4 = "plpala" wide ascii nocase
  condition:
    4 of ($o*)
}