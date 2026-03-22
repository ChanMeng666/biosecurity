import * as React from "react"

interface SlotProps extends React.HTMLAttributes<HTMLElement> {
  children?: React.ReactNode
}

const Slot = React.forwardRef<HTMLElement, SlotProps>(
  ({ children, ...props }, ref) => {
    if (React.isValidElement(children)) {
      const childProps = children.props as Record<string, unknown>
      return React.cloneElement(
        children as React.ReactElement<Record<string, unknown>>,
        {
          ...props,
          ...childProps,
          ref,
          className: [props.className, childProps.className].filter(Boolean).join(" "),
        }
      )
    }

    return null
  }
)
Slot.displayName = "Slot"

export { Slot }
