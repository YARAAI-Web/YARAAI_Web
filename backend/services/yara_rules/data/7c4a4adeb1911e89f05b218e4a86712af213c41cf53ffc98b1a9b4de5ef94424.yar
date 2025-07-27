rule auto_rule_20250726200932_0521 {
  strings:
    $o0 = "dword_427CCC" wide ascii nocase
    $o1 = "dword_427E0C" wide ascii nocase
    $o2 = "ActiveWindow" wide ascii nocase
    $o3 = "dword_427528" wide ascii nocase
    $o4 = "byte_427FA1" wide ascii nocase
  condition:
    4 of ($o*)
}